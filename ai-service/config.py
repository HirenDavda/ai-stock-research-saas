import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# APP SETTINGS
# =========================

APP_NAME = "AI Stock Research API"
APP_VERSION = "1.0.0"

# =========================
# API KEYS
# =========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =========================
# LLM SETTINGS
# =========================

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", 0.2)
)

# =========================
# EMBEDDINGS
# =========================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "models/embedding-001"
)

OPENAI_CHAT_MODEL = os.getenv(
    "OPENAI_CHAT_MODEL",
    "gemini-2.5-flash"
)

# =========================
# RAG SETTINGS
# =========================

RAG_TOP_K = int(
    os.getenv("RAG_TOP_K", 4)
)


# =========================
# VECTOR DB
# =========================

CHROMA_DIR = os.getenv(
    "CHROMA_DIR",
    "chroma_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "financial_documents"
)

# =========================
# MONGODB SETTINGS
# =========================

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"
)

MONGO_DB_NAME = os.getenv(
    "MONGO_DB_NAME",
    "ai_stock_db"
)

MONGO_DOC_COLLECTION = os.getenv(
    "MONGO_DOC_COLLECTION",
    "documents"
)

# =========================
# SERVER
# =========================

HOST = "0.0.0.0"

PORT = int(
    os.getenv("PORT", "8000")
)
