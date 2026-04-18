from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from services.chat_with_docs import ask_question # only to reuse pipeline structure
from database.vector_store import save_document_chunks
from services.embedding_service import get_embedding

router = APIRouter()

@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    try: 
        content = await file.read()
        text = content.decode("utf-8", errors="ignore") 

        if not text.strip():
            raise HTTPException(status_code=400, detail="Empty file")

        # simple chunking (minimal safe version)
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]    

        embeddings = [get_embedding(c) for c in chunks]

        doc_id = file.filename or "doc"

        chunk_ids = save_document_chunks(
            document_id=doc_id,
            chunks=chunks,
            embeddings=embeddings,
            metadata=[{"source": doc_id}] * len(chunks)
        )

        return {
            "message": "Document uploaded successfully",
            "document_id": doc_id,
            "chunks_created": len(chunk_ids)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))