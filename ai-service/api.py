from fastapi import APIRouter
from pydantic import BaseModel

from services.chat_with_docs import ask_question

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat")
def chat(request: QuestionRequest):

    print("Received question:", request.question)

    try:
        result = ask_question(request.question)

        print("Result from ask_question:", result)

        return {
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception as e:

        print("ERROR in /chat:")
        print(str(e))

        return {
            "error": str(e)
        }