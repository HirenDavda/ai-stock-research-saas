from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.chat_with_docs import ask_question

router = APIRouter()

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    sources: list

@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    """
    Ask a question against ingested documents.
    """

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )
        
    try:
        result = ask_question(question)

        return {
            "answer": result.get("answer", ""),
            "sources": result.get("sources", [])
        }  

    except Exception as e:    
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )      
