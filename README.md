# AI Stock Research SaaS

AI-powered platform that allows investors to chat with annual reports and earnings transcripts using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features (MVP)
1 Chat with annual reports
2 AI-generated company summaries
3 Source citation from documents
4 Document ingestion pipeline

---

## 🏗️ Architecture

Frontend → Backend API → AI RAG Service → Vector Database

Components:
1 Frontend: Next.js
2 Backend: Node.js / Express
3 AI Service: Python + LangChain
4 Vector Database: Chroma
5 LLM: OpenAI API

---

### Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Next.js |
| **Backend** | Node.js / Express |
| **AI Service** | Python + LangChain |
| **Vector DB** | Chroma |
| **LLM** | OpenAI API |

---

## 📁 Project Structure

ai-stock-research-saas
│
├── frontend
├── backend
├── ai-service
├── infrastructure
│   ├── docker
│   └── kubernetes
└── docs

->->->->->->->->->->->->->->->->->->->->->

Prerequisites

Install the following tools:
Node.js (v22.14.0)
Python (3.10.11)
Docker
Git

->->->->->->->->->->->->->->->->->->->->->

Local Development Setup

1 Clone repository
2 Start frontend
3 Start backend
4 Start AI service

->->->->->->->->->->->->->->->->->->->->->

Environment Variables

Create a .env file in the root of each service.
Note: Never commit .env files to version control.

Example (ai-service/.env):
OPENAI_API_KEY=your_key_here
DATABASE_URL=your_db_url

->->->->->->->->->->->->->->->->->->->->->

Development Workflow

We follow a standard branching strategy:

main → production
develop → staging
feature/* → development (e.g., feature/rag-ingestion, feature/chat-ui)

->->->->->->->->->->->->->->->->->->->->->

Future Features
1 Earnings Call Analysis: Real-time sentiment tracking.
2 Risk Detection: Automated flagging of financial red flags.
3 Portfolio monitoring agent: Autonomous monitoring for specific stock triggers.