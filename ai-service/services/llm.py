from config import MODEL_NAME, TEMPERATURE
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    
    llm = ChatGoogleGenerativeAI(
        model = MODEL_NAME,
        temperature = TEMPERATURE
    )

    return llm