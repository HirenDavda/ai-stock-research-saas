# AI Stock Research SaaS – Project Context

## 🎯 Goal
Build an AI-powered SaaS where retail investors can:
- Chat with annual reports
- Get financial insights
- See source-backed answers

---

## 🧠 Core Architecture
Frontend → Backend (Node.js) → AI Service (Python RAG) → Vector DB

---

## 🛠 Tech Stack

Frontend:
- Next.js
- React
- Tailwind

Backend:
- Node.js
- Express

AI Service:
- Python
- LangChain
- OpenAI API
- Chroma Vector DB

Infra:
- Docker (planned)
- Kubernetes (later)

---

## ✅ Completed Work (Day 1–5)

### Day 1
- Project structure created
- GitHub repo setup
- Frontend, backend, AI service initialized

### Day 2
- PDF loader implemented using PyPDF
- Successfully extracted text from annual report

### Day 3
- Document chunking implemented
- Optimized chunk size (2000 / overlap 300)
- Created ~496 chunks (Dodla Dairy report)

### Day 4
- Created embeddings using OpenAI
- Stored in Chroma vector DB
- Implemented semantic search

### Day 5
- Built RAG-based chat system
- Vector search + LLM answer generation
- Added prompt to reduce hallucination
- Displayed sources

---

## 📂 Current Capabilities

System can:
- Read annual reports
- Convert into chunks
- Store embeddings
- Search relevant information
- Generate AI answers from documents

---

## ⚠️ Important Decisions

- db/ folder is NOT pushed to Git
- requirements.txt is maintained
- Using langchain-chroma (latest)
- Using environment variables for API keys

---

## 🚀 Next Steps

Day 6:
- Create backend API (POST /chat)
- Connect Node.js → Python AI service

Day 7:
- Connect frontend chat UI

Day 8+:
- Add company selector
- Improve UI/UX
- Add deployment

---

## 🧩 Current Task

Continue development from:
👉 Day 6 – Backend API integration with AI service

---

## 🎯 Instruction for AI Assistant

Act as:
- Senior AI Systems Engineer
- Guide step-by-step
- Give code with simple comments
- Update only required code (not full rewrite)

## 🎯 Workflow
Cursor → code editing
ChatGPT → architecture guidance
GitHub → version control
Context file → memory