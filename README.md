AI Stock Research SaaS

AI-powered platform that allows investors to chat with annual reports and earnings transcripts using Retrieval-Augmented Generation (RAG).

->->->->->->->->->->->->->->->->->->->->->

Features (MVP)
1 Chat with annual reports
2 AI-generated company summaries
3 Source citation from documents
4 Document ingestion pipeline

->->->->->->->->->->->->->->->->->->->->->

Architecture

Frontend → Backend API → AI RAG Service → Vector Database

Components:
1 Frontend: Next.js
2 Backend: Node.js / Express
3 AI Service: Python + LangChain
4 Vector Database: Chroma
5 LLM: OpenAI API

->->->->->->->->->->->->->->->->->->->->->

Project Structure

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
Node.js
Python
Docker
Git

->->->->->->->->->->->->->->->->->->->->->

Local Development Setup

Clone repository

Start frontend

Start backend

Start AI service

->->->->->->->->->->->->->->->->->->->->->

Environment Variables

Create .env files for services.

Example:
OPENAI_API_KEY=your_key_here

Never commit .env files.

->->->->->->->->->->->->->->->->->->->->->

Development Workflow
main → production
develop → staging
feature/* → development

Example:
feature/rag-ingestion
feature/chat-ui

->->->->->->->->->->->->->->->->->->->->->

Future Features
1 earnings call analysis
2 risk detection
3 portfolio monitoring agent