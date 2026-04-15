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

## Folder Structure
/ai-service
    /services
        - embedding_service.py
        - chunking_service.py
    /scripts
        - test_search.py
        - test_vector_store.py
    /db
        - chroma_store.py
        - mongo.py
    /database
    /vector_store
        - base.py
        - factory.py
    requirements.txt
    .env
/backend
/docs
/frontend
/infrastructure

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
- Sentence Transformers
- Chroma Vector DB

Database Design:
- DB name
- Collections / tables
- Schema structure

Vector Database (Current)
- ChromaDB (Local testing)

Vector Database (Future Options)
- MongoDB Atlas Vector Search
- Pinecone
- Weaviate
- FAISS

Other:
- Git
- Virtual Environment (venv)
- REST API
- JSON

Infrastructure:
- Docker (planned)
- Kubernetes (later)
- CI/CD pipeline

---

## Database Design

### Vector Database

Current:

ChromaDB (Local)

Purpose:

Store:

- document chunks
- embeddings
- metadata

Core Operations:

- add document chunks
- search embeddings
- return relevant results

### Metadata Database (Future)

MongoDB Atlas

Purpose:

Store:

- document metadata
- user data
- upload history
- processing status

---

### Data Flow

Document
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Store
   ↓
Search
   ↓
LLM Answer

---

## Important Rules

Strict Engineering Rules:
- Do not rename functions
- Do not modify DB layer logic
- Do not refactor working components
- Fix errors with minimal patch only
- Keep imports stable
- Keep folder structure stable
- Maintain backward compatibility
- Use Git commit after every working fix
- db/ folder must not be pushed to Git
- Use environment variables for secrets
- Update context file only after feature is stable
- Keep API contracts stable
- Never re-explain project. Always update project and active task context file instead. 

Operational Rules:
- Always fix one error at a time
- Always run test after change
- Never mix Mongo and Chroma logic in same file
- Database must be replaceable without changing business logic
- Keep vector store swappable

---

## ✅ Completed Work (Day 1–5)

## Day 1
- Project structure created
- Git repository initialized
- Frontend / Backend / AI service setup

## Day 2
- PDF loader implemented
- Text extraction working

## Day 3
- Document chunking implemented
- Chunk optimization completed

## Day 4
- Embedding generation implemented
- Vector storage implemented

## Day 5
- RAG pipeline implemented
- Semantic search working
- LLM answer generation working
- Source display implemented

## Day 6
- Backend API integration started

## Day 7
- MongoDB metadata testing

## Day 8
- Vector database migration initiated

## Day 9
- ChromaDB integrated for local testing

## Day 10
- Embedding service stabilized

## Day 11
- Search testing implemented

## Day 12
- MongoDB Atlas temporarily replaced with ChromaDB for local testing
- Import and module path issues identified and fixed

---

## Current System Capabilities

System can:
- Read financial documents
- Create chunks
- Generate embeddings
- Store embeddings
- Perform semantic search
- Return relevant document context
- Run local vector database
- Support future database migration

Verified (2026-04-14):
- Local script flow works end-to-end:
  - `scripts/test_chunking.py`
  - `scripts/test_document_loader.py`
  - `scripts/test_embedding.py`
  - `scripts/test_vector_store.py` (writes to local Chroma collection via raw client)
  - `scripts/test_search.py` (reads from local Chroma collection via raw client)
- `services/chat_with_docs.ask_question()` retrieves from the same raw Chroma collection and returns:
  - `answer` (LLM output text)
  - `sources` (list of `{text, metadata}`)

Known constraint / current blocker:
- FastAPI app import/run requires dependencies installed in the active Python environment.
  - If you see `ModuleNotFoundError: fastapi` from `ai-service/main.py`, create/activate venv and install:
    - `python3 -m venv .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`

---

## Future Direction

- Stabilize vector search pipeline
- Add API endpoint integration
- Connect frontend chat UI
- Implement authentication
- Deploy production system

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
- Cursor → code editing
- ChatGPT → architecture guidance
- GitHub → version control
- Context file → memory


