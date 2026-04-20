const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const mongoose = require('mongoose');
const { v4: uuidv4 } = require('uuid');
const chatRoute = require('./routes/chat');

// Load environment variables
dotenv.config();

// Allow requests from other applications (like our frontend)
const app = express();
app.use(cors());

// Allow server to understand JSON data sent in requests
app.use(express.json());

app.use((req, res, next) => {
  const requestId = uuidv4();

  req.requestId = requestId;

  console.log(`[REQUEST] ${requestId} ${req.method} ${req.url}`);

  next();
});

// Chat route
app.use("/chat", chatRoute);

const PORT = Number(process.env.PORT || 5001);
const PYTHON_SERVICE_URL = process.env.PYTHON_SERVICE_URL || 'http://localhost:8000';
const MONGO_URI = process.env.MONGO_URI || '';

if (!MONGO_URI) {
  console.warn('MONGO_URI missing; document/job persistence is disabled.');
} else {
  mongoose
    .connect(MONGO_URI)
    .then(() => console.log('MongoDB connected'))
    .catch((error) => console.error('MongoDB connection failed', error));
}

const documentSchema = new mongoose.Schema(
  {
    documentId: { type: String, unique: true, index: true, required: true },
    originalFileName: { type: String, required: true },
    storagePath: { type: String, required: true },
    status: { type: String, enum: ['QUEUED', 'PROCESSING', 'COMPLETED', 'FAILED'], default: 'QUEUED' },
    jobId: { type: String },
    error: { type: String },
    chunksIndexed: { type: Number },
  },
  { timestamps: true }
);

const jobSchema = new mongoose.Schema(
  {
    jobId: { type: String, unique: true, index: true, required: true },
    documentId: { type: String, required: true },
    status: { type: String, enum: ['QUEUED', 'PROCESSING', 'COMPLETED', 'FAILED'], default: 'QUEUED' },
    error: { type: String },
  },
  { timestamps: true }
);

const Document = mongoose.models.Document || mongoose.model('Document', documentSchema);
const Job = mongoose.models.Job || mongoose.model('Job', jobSchema);

const uploadsDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadsDir)) {
  fs.mkdirSync(uploadsDir, { recursive: true });
}

const upload = multer({ dest: uploadsDir });

const queue = [];
let isProcessingJob = false;

const enqueueJob = (job) => {
  queue.push(job);
  processQueue().catch((error) => {
    console.error('Queue processing error', error);
  });
};

const processQueue = async () => {
  if (isProcessingJob || queue.length === 0) return;
  isProcessingJob = true;

  const job = queue.shift();
  try {
    await Job.updateOne({ jobId: job.jobId }, { $set: { status: 'PROCESSING' } });
    await Document.updateOne(
      { documentId: job.documentId },
      { $set: { status: 'PROCESSING', jobId: job.jobId } }
    );

    await axios.post(
      `${PYTHON_SERVICE_URL}/documents/process`,
      {
        job_id: job.jobId,
        document_id: job.documentId,
        file_path: job.filePath,
        source_file: job.sourceFile,
      },
      { timeout: 0 }
    );

    await Job.updateOne({ jobId: job.jobId }, { $set: { status: 'COMPLETED' } });
  } catch (error) {
    const message = error?.response?.data?.detail || error.message || 'Unknown processing error';
    await Job.updateOne({ jobId: job.jobId }, { $set: { status: 'FAILED', error: message } });
    await Document.updateOne(
      { documentId: job.documentId },
      { $set: { status: 'FAILED', error: message } }
    );
  } finally {
    isProcessingJob = false;
    if (queue.length > 0) {
      setImmediate(() => {
        processQueue().catch((error) => console.error('Queue processing error', error));
      });
    }
  }
};

app.get('/', (req, res) => {
  res.send('Stock AI Backend Running');
});

app.post('/api/chat/stream', async (req, res) => {
  const { question, documentId, topK } = req.body || {};

  if (!question) {
    return res.status(400).json({ error: 'question is required' });
  }

  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.flushHeaders?.();

  const controller = new AbortController();
  req.on('close', () => controller.abort());

  try {
    const response = await axios.post(
      `${PYTHON_SERVICE_URL}/chat/stream`,
      {
        question,
        document_id: documentId || null,
        top_k: topK,
      },
      {
        responseType: 'stream',
        signal: controller.signal,
        timeout: 0,
      }
    );

    response.data.on('data', (chunk) => {
      res.write(chunk);
    });

    response.data.on('end', () => {
      res.end();
    });

    response.data.on('error', (error) => {
      res.write(`event: error\ndata: ${JSON.stringify({ error: error.message })}\n\n`);
      res.end();
    });
  } catch (error) {
    const message = error?.response?.data?.detail || error.message || 'Streaming proxy failed';
    res.write(`event: error\ndata: ${JSON.stringify({ error: message })}\n\n`);
    res.end();
  }
});

app.post('/api/documents/upload', upload.single('file'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'file is required' });
  }

  const documentId = uuidv4();
  const jobId = uuidv4();

  await Document.create({
    documentId,
    originalFileName: req.file.originalname,
    storagePath: req.file.path,
    status: 'QUEUED',
    jobId,
  });

  await Job.create({
    jobId,
    documentId,
    status: 'QUEUED',
  });

  enqueueJob({
    jobId,
    documentId,
    filePath: req.file.path,
    sourceFile: req.file.originalname,
  });

  return res.status(202).json({
    jobId,
    documentId,
    status: 'QUEUED',
  });
});

app.get('/api/jobs/:jobId', async (req, res) => {
  const job = await Job.findOne({ jobId: req.params.jobId }).lean();
  if (!job) {
    return res.status(404).json({ error: 'job not found' });
  }
  return res.json(job);
});

app.get('/api/documents/:documentId', async (req, res) => {
  const document = await Document.findOne({ documentId: req.params.documentId }).lean();
  if (!document) {
    return res.status(404).json({ error: 'document not found' });
  }
  return res.json(document);
});

// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });

app.get("/", (req, res) => {
  res.send("Root working");
});

app.get("/health", (req, res) => {
  res.json({
    success: true,
    data: {
        status: "ok",
        service: "node-backend",
        timestamp: new Date().toISOString()
    },
    error: null
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});