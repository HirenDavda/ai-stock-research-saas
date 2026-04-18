from fastapi import APIRouter
from .chat import router as chat_router
from .upload import router as upload_router
from .health import router as health_router

api_router = APIRouter()

# Combine them all here
api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])
api_router.include_router(health_router, prefix="/health", tags=["Health"])