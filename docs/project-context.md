# AI Stock Research SaaS — Project Context

## Product Goal

Build an AI-powered research assistant for retail investors to:

* Upload financial documents
* Ask questions in natural language
* Receive source-backed answers

Architecture Flow:

Frontend → Node.js Backend → Python AI Service (RAG) → Chroma Vector Database

---

# Current System Architecture

## Python AI Service (ai-service)

Core Responsibilities:

* Document ingestion
* Chunking
* Embedding generation
* Vector storage
* Semantic search
* RAG answer generation
* API endpoints
* Logging and monitoring

---

## Technology Stack

Backend:

* Python 3.10
* FastAPI

Embeddings:

* sentence-transformers
* Model: all-MiniLM-L6-v2
* Local inference

Vector Database:

* ChromaDB
* Local persistent storage

LLM:

* Google Gemini API

Infrastructure:

* Mac M1
* 8GB RAM
* Local development environment

---

# Folder Structure

ai-stock-research-saas/

ai-service/

api/

routes/

chat.py

upload.py

health.py

services/

chat_with_docs.py

embedding_service.py

logger.py

database/

chroma_client.py

vector_store.py

scripts/

smoke_test.py

test_vector_store.py

test_search.py

main.py

requirements.txt

chroma_db/

---

# Verified System Status

Document ingestion: PASS

Vector storage persistence: PASS

Semantic search: PASS

RAG answer generation: PASS

Logging system: PASS

Health endpoint: PASS

Error handling: PASS

API smoke test: PASS

---

# Definition of Feature 1 — DONE

User uploads document

User asks question

System answers from document

Sources returned

Data persists after restart

Server runs without error

Logging captures activity

Health endpoint responds

Errors handled safely

---

# Current Development Stage

Phase:

Feature 1 — Core RAG Engine

Status:

100% Complete

---

# Next Major Milestone

Node ↔ Python Integration

Goal:

Node backend communicates with Python AI service

---

# Future Roadmap

Phase 2

* Multi-document support
* User workspace
* Document management

Phase 3

* Frontend UI
* Chat interface
* Upload interface

Phase 4

* Production deployment
* Authentication
* Cloud hosting
* Monitoring

---

# Engineering Principles

* Minimal architecture
* Production-safe patterns
* Local-first development
* Cost-efficient infrastructure
* Incremental feature delivery
