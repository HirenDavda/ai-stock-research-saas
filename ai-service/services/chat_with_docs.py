import os
from dotenv import load_dotenv

# Import embedding model (converts text to meaning-based numbers)
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Import vector database (where our document knowledge is stored)
from langchain_chroma import Chroma

# Import Chat model (this generates final human-like answers)
# from langchain_openai import ChatOpenAI

from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables (API key)
load_dotenv()


# Function to answer user question
def ask_question(question):
    # Step 1: Load embedding model
    # This helps search similar meaning text in our document database
    
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Step 2: Load vector database (Chroma)
    # This is where we stored our document knowledge as vectors
    vector_db = Chroma(
        persist_directory="./chroma_db",  # Path to our vector database
        embedding_function=embeddings,    # Use our embedding model
    )

    # Step 3: Search top relevant chunks from vector database
    # This retrieves the most relevant pieces of information based on the question
    results = vector_db.similarity_search(
        question, 
        k=3
    )  # Get top 3 relevant chunks

    # Combine all retrieved chunks into one context string
    context = "\n\n".join([doc.page_content for doc in results])


    # Step 4: Create LLM (AI model)
    # llm = ChatOpenAI(
    #     model="gpt-3.5-turbo",  # Use GPT-3.5 Turbo model
    #     temperature=0.2,        # Lower temperature for more focused answers
    # )

    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

    llm = ChatGoogleGenerativeAI(
        model = MODEL_NAME,
        temperature = TEMPERATURE
    )
    
    # Step 5: Create prompt (instructions for AI)
    prompt = f"""
You are a financial research assistant.

Rules:
- Answer ONLY from the provided context
- Do NOT make up information
- If unsure, say "Not found in document"
- Keep answers clear and structured

Context:
{context}

Question:
{question}
"""

    # Step 6: Generate answer
    response = llm.invoke(prompt)

    # Print answer    
    print("\nSources:\n")

    for i, doc in enumerate(results):
        print(f"Source {i+1}:\n")
        print(doc.page_content[:300])

    print("\nAI Answer:\n")
    print(response.content)

    return {
        "answer": answer,
        "sources": sources
    }

# Run test
if __name__ == "__main__":
    ask_question("What are the risks mentioned by the company?")
    