"""
MongoDB connection and collection utilities
"""

from pymongo import MongoClient
from config import (
    MONGO_URI,
    MONGO_DB_NAME,
    MONGO_DOC_COLLECTION
)

# Global client instance for MongoDB
mongo_client: MongoClient | None = None

def connect_to_mongo():
    """
    Initialize MongoDB connection
    Called during FastAPI startup
    """

    global mongo_client

    if mongo_client is None:
        mongo_client = MongoClient(MONGO_URI)
        print("MongoDB connected successfully")

    return mongo_client

def close_mongo_connection():
    """
    Close MongoDB connection
    Called during FastAPI shutdown
    """

    global mongo_client

    if mongo_client:
        mongo_client.close()
        mongo_client = None
        print("MongoDB connection closed")

def get_database():
    """
    Get MongoDB database instance
    """

    if mongo_client is None:
        raise RuntimeError("MongoDB not connected")

    return mongo_client[MONGO_DB_NAME]

def get_document_collection():
    """
    Get documents collection
    """
    db = get_database()
    return db[MONGO_DOC_COLLECTION]                
