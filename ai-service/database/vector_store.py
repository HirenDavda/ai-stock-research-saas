from datetime import datetime

from database.mongo import get_database
from database.chroma_client import collection

from services.embedding_service import get_embedding_model

COLLECTION_NAME = "document_chunks"

def get_chunks_collection():

    db = get_database()

    return db[COLLECTION_NAME]

def save_document_chunks(document_id, chunks, embeddings, metadata):
    """
    Save document chunks and embeddings to ChromaDB
    """

    ids = [f"{document_id}_{i}" for i in range(len(chunks))]
    embeddings = get_embedding_model().encode(chunks).tolist()
    
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadata
    )
    
    print("Chunks saved to ChromaDB")
    
    return ids


def create_indexes():

    collection = get_chunks_collection()

    collection.create_index(
        [("document_id", 1)]
    )    

    collection.create_index(
        [("chunk_index", 1)]
    )

    print("Indexes created")