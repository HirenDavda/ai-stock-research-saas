import json
import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from api import router
from services.llm import get_llm
from config import (
    MODEL_NAME,
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    OPENAI_CHAT_MODEL,
    RAG_TOP_K,
    MONGO_URI,
    MONGO_DB_NAME,
    MONGO_DOC_COLLECTION,
)

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel, Field
from pymongo import MongoClient
from database.mongo import (
    connect_to_mongo,
    close_mongo_connection,
)

# -----------------------------------------------------
# Logging Setup
# -----------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------------------------------
# Startup Initialization (Performance Optimization)
# -----------------------------------------------------
@asynccontextmanager
async def lifespan(app):
    # Startup
    connect_to_mongo()
    print("Application startup complete")

    yield

    # Shutdown
    close_mongo_connection()
    print("Application shutdown complete")
    logger.info("Application shutdown complete")
    
    """
    Application startup and shutdown handler
    """

    try:
        logger.info("Starting AI Stock Research API...")

        # Initialize Vector DB
        from services.vector_store import get_vector_store
        
        vector_db = get_vector_store()

        # Initialize LLM
        from services.llm import get_llm

        llm = get_llm()

        # Store in app state
        app.state.vector_db = vector_db
        app.state.llm = llm

        logger.info("Startup complete")

        yield

    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise

    finally:
        logger.info("Shutting down application")

# -----------------------------------------------------
# FastAPI App Initialization
# -----------------------------------------------------
app = FastAPI(
    title="AI Stock Research API",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS (required for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api")


# -----------------------------------------------------
# Request Models
# -----------------------------------------------------
class ChatStreamRequest(BaseModel):
    question: str = Field(..., min_length=1)
    document_id: str | None = None
    top_k: int = Field(default=RAG_TOP_K, ge=1, le=10)


class ProcessDocumentRequest(BaseModel):
    job_id: str = Field(..., min_length=1)
    document_id: str = Field(..., min_length=1)
    file_path: str = Field(..., min_length=1)
    source_file: str = Field(..., min_length=1)





# -----------------------------------------------------
# Utility Functions
# -----------------------------------------------------
def _build_metadata(docs: list[Any]) -> list[dict[str, Any]]:
    citations: list[dict[str, Any]] = []

    for doc in docs:
        doc_meta = doc.metadata or {}
        snippet = doc.page_content[:220].strip()

        citations.append(
            {
                "source_file": doc_meta.get("source_file")
                or doc_meta.get("source")
                or "unknown",
                "page_number": doc_meta.get("page_number"),
                "snippet": snippet,
            }
        )

    return citations


def _update_document_status(
    document_id: str,
    status: str,
    extra: dict[str, Any] | None = None,
) -> None:
    if not MONGO_URI:
        return

    payload: dict[str, Any] = {"status": status}

    if extra:
        payload.update(extra)

    try:
        with MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000) as client:
            collection = client[MONGO_DB_NAME][MONGO_DOC_COLLECTION]
            collection.update_one(
                {"documentId": document_id},
                {"$set": payload},
                upsert=False,
            )

    except Exception:
        logger.error("Failed to update document status", exc_info=True)


# -----------------------------------------------------
# Health Check Endpoint (Production Requirement)
# -----------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "ai-stock-research-service",
    }


# -----------------------------------------------------
# Root Endpoint
# -----------------------------------------------------
@app.get("/")
def home():
    return {"message": "AI Service Running!"}


# -----------------------------------------------------
# Streaming Chat Endpoint
# -----------------------------------------------------
@app.post("/chat/stream")
async def chat_stream(payload: ChatStreamRequest) -> StreamingResponse:

    try:
        vector_db = app.state.vector_db

        where_clause = (
            {"document_id": payload.document_id}
            if payload.document_id
            else None
        )

        docs = vector_db.similarity_search(
            payload.question,
            k=payload.top_k,
            filter=where_clause,
        )

        citations = _build_metadata(docs)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

    except Exception as exc:
        logger.error("Retrieval failed", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Retrieval failed: {exc}",
        ) from exc

    if not context:
        citations = []
        context = "No relevant context found."

    prompt = f"""
You are a financial research assistant.
Answer only from the supplied context.
If the answer is missing, say 'Not found in document.'

Context:
{context}

Question:
{payload.question}
""".strip()

    llm = app.state.llm

    async def token_event_stream():
        try:
            async for chunk in llm.astream(prompt):
                token = getattr(chunk, "content", "") or ""

                if token:
                    yield (
                        f"data: {json.dumps({'type': 'token', 'token': token})}\n\n"
                    )

            yield (
                f"data: {json.dumps({'type': 'metadata', 'metadata': citations})}\n\n"
            )

            yield "data: [DONE]\n\n"

        except Exception as exc:
            logger.error("Streaming failed", exc_info=True)

            yield (
                f"event: error\n"
                f"data: {json.dumps({'error': str(exc)})}\n\n"
            )

    return StreamingResponse(
        token_event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# -----------------------------------------------------
# Document Processing Endpoint
# -----------------------------------------------------
@app.post("/documents/process")
def process_document(payload: ProcessDocumentRequest) -> dict[str, str]:

    _update_document_status(
        payload.document_id,
        "PROCESSING",
        {"jobId": payload.job_id},
    )

    try:
        loader = PyPDFLoader(payload.file_path)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=200,
        )

        chunks = splitter.split_documents(pages)

        for chunk in chunks:
            chunk.metadata = {
                **(chunk.metadata or {}),
                "document_id": payload.document_id,
                "source_file": payload.source_file,
                "page_number": (
                    chunk.metadata.get("page", 0) + 1
                    if chunk.metadata
                    else None
                ),
                "snippet": chunk.page_content[:220].strip(),
            }

        vector_db = app.state.vector_db

        vector_db.add_documents(chunks)
        vector_db.persist()

        _update_document_status(
            payload.document_id,
            "COMPLETED",
            {
                "jobId": payload.job_id,
                "chunksIndexed": len(chunks),
            },
        )

        return {"status": "COMPLETED"}

    except Exception as exc:
        logger.error("Document processing failed", exc_info=True)

        _update_document_status(
            payload.document_id,
            "FAILED",
            {
                "jobId": payload.job_id,
                "error": str(exc),
            },
        )

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {exc}",
        ) from exc


if __name__ == "__main__":
    import uvicorn
    from config import HOST, PORT

    print("Starting AI Stock Research API...")

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True
    )

    