# AI Stock Research SaaS — Project Status File

**Project:** AI Stock Research Application (RAG-based SaaS)
**Owner:** Hiren
**Current Phase:** Backend Integration — Day 6 Completed (Infrastructure Level)
**Date:** Current Session End

---

## 1) Summary of Current Progress (What Was Completed Up to Day 6)

### Core System Infrastructure

The backend system for the AI Stock Research SaaS has been successfully established and integrated. All major services are now running and communicating correctly.

Completed components:

- FastAPI AI service running on **port 8000**
- Node.js backend server running on **port 5001**
- Port conflict on 5000 identified and resolved
- Health endpoint `/health` verified and operational
- Node → FastAPI communication confirmed
- Environment configuration using `.env`
- Curl-based integration testing completed

### RAG (Retrieval-Augmented Generation) Pipeline

The core AI pipeline structure is implemented.

Completed:

- Document ingestion pipeline created
- Vector database (`db/`) successfully generated
- Chroma persistence verified
- Embedding model loading confirmed
- Retrieval pipeline initialized
- Chat endpoint routing operational

Verified components:

- Embedding model loads at startup
- Vector database detected
- API request flow working end-to-end

Current status:

Infrastructure works. Chat logic returns a runtime error that is under debugging.

### System Architecture Achieved

Client
   ↓
Node.js Backend (Express)
   ↓
FastAPI AI Service
   ↓
Chroma Vector Database
   ↓
Embedding Model
   ↓
LLM Response

This architecture is now production-aligned for a scalable AI research system.

---

## 2) Specific Technical Decisions Made

### Backend Framework

FastAPI

Reasons:

- High performance
- Async support
- Simple API development
- Production-ready

### Backend Gateway / Orchestration Layer

Express.js (Node.js)

Reasons:

- Lightweight API layer
- Easy integration
- Common SaaS backend pattern
- Works well as service orchestrator

### Vector Database

Chroma

Reasons:

- Local persistence
- Fast development setup
- No external infrastructure required
- Easy migration to cloud vector databases later

Future migration options:

- Pinecone
- Weaviate
- Qdrant

### Embedding Model

sentence-transformers/all-MiniLM-L6-v2

Reasons:

- Lightweight
- Fast
- Free to run locally
- Proven for RAG systems

### Project Structure Decision

ai-stock-research-saas/

backend/
    server.js
    routes/

ai-service/
    api.py
    scripts/
        chat_with_docs.py
        ingest.py

    db/
    data/

### Port Allocation

5001 → Node Backend

8000 → FastAPI AI Service

Reason:

Avoid macOS system port conflicts.

### Chunking Strategy

chunk_size = 1000
chunk_overlap = 200

Reason:

Balance between:

- Retrieval accuracy
- Token efficiency
- Performance

---

## 3) Next Steps — Day 7

### Primary Goal

Implement Document Upload API and automated ingestion workflow.

### Feature 1 — Upload API

Endpoint:

POST /upload

Responsibilities:

- Accept PDF file
- Validate file
- Save file to data folder
- Trigger ingestion process

### Feature 2 — Automatic Ingestion Trigger

Workflow:

Upload file
     ↓
Save to data/
     ↓
Run ingest.py
     ↓
Update vector database

### Feature 3 — Job Status Tracking (Preparation for Scale)

Future endpoints:

POST /upload

GET /job-status/:id

This prepares the system for:

- Large documents
- Multiple users
- Background processing

### Day 7 Deliverables

- File upload route implemented
- File storage working
- Ingestion triggered automatically
- New documents searchable
- Error-safe processing

---

## 4) Known Bugs or Pending Tasks

### Active Bug

Issue:

POST /chat returns 500 Internal Server Error

Observed behavior:

- Request reaches FastAPI
- Embedding model loads
- Vector database exists
- Exception occurs during question processing

Likely root causes:

- ask_question() return format mismatch
- Retriever initialization issue
- Empty retrieval result handling
- Exception inside LangChain pipeline

Status:

Infrastructure is working. Debugging is focused on application logic.

---

### Pending Tasks

Fix chat endpoint runtime error

Add structured error logging

Validate ask_question() return format

Implement upload API

Add file validation

Add request validation

Add logging middleware

Add production configuration support

---

## Operational Readiness Status

Infrastructure: COMPLETE

Core Architecture: COMPLETE

Integration Layer: COMPLETE

Application Logic: IN PROGRESS

---

## Next Session Starting Point

Start from:

Day 7 — Document Upload API Implementation

