"""
MongoDB connection and collection utilities
"""

from pymongo import MongoClient
from dotenv import load_dotenv

import os

from config import (
    MONGO_URI,
    MONGO_DB_NAME,
    MONGO_DOC_COLLECTION
)

from datetime import datetime
from bson import ObjectId


client = None
db = None
collection = None


def connect_to_mongo():

    global client
    global db

    print("STEP 1 — Loading environment variables...")
    load_dotenv()

    mongo_uri = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017"
    )

    print("STEP 2 — Mongo URI:", mongo_uri)

    try:

        print("STEP 3 — Attempting MongoDB connection...")

        client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000
        )
        print("STEP 4 — Forcing connection test")
        # Force connection test
        client.server_info()
        print("STEP 5 — Selecting database")
        db = client[MONGO_DB_NAME]
        print("STEP 6 — MongoDB connected successfully")

    except Exception as e:

        print("MongoDB connection failed")
        print("Error:", e)

        db = None

def close_mongo_connection():
    """
    Close MongoDB connection
    Called during FastAPI shutdown
    """

    global client

    if client:
        client.close()
        client = None
        print("MongoDB connection closed")

def get_database():
    """
    Get MongoDB database instance
    """

    if db is None:
        print("Database not initialized — connecting now...")
        connect_to_mongo()
    
    return db

    # if mongo_client is None:
    #     raise RuntimeError("MongoDB not connected")

    # return mongo_client[MONGO_DB_NAME]

def get_document_collection():
    """
    Get documents collection
    """
    db = get_database()
    return db[MONGO_DOC_COLLECTION]                

def save_document_metadata(
    filename: str,
    file_path: str,
    chunks: int,
    file_size: int,
    content_type: str
):
    """
    Save document metadata to MongoDB
    """

    collection = get_document_collection()
    
    document = {
        "filename": filename,
        "file_path": file_path,
        "file_size": file_size,
        "content_type": content_type,

        "status": "uploaded",

        "upload_time": datetime.utcnow(),

        "chunks_count": chunks,

        "embedding_model": None,

        "processed": False,

        "error": None,

        "user_id": None,   
        
        "created_at": datetime.utcnow(),

        "updated_at": datetime.utcnow(),    
    }

    result = collection.insert_one(document)

    doc_id = str(result.inserted_id)

    print("Document metadata saved:", doc_id)    

    return doc_id
  

def get_all_documents():
    """
    Get list of all uploaded documents
    """

    collection = get_document_collection()

    documents = []

    for doc in collection.find({ "status": "uploaded" }):
        documents.append(
            {
                "id": str(doc["_id"]),
                "filename": doc["filename"],
                "chunks": doc["chunks_count"],
                "uploaded_at": doc["upload_time"],
            }
        )
    return documents    

def delete_document_metadata(document_id: str):
    """
    Soft delete document
    """

    collection = get_document_collection()

    result = collection.update_one(
        { "_id": ObjectId(document_id) },
        { 
            "$set": {
                "status": "deleted",
                "deleted_at": datetime.utcnow(),
            } 
        },
    )

    return result.modified_count
