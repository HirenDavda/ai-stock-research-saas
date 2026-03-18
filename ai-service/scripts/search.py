# Import embedding model from OpenAI
# This converts text into numbers (vectors)
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Import Chroma vector database
# This stores and searches embeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
import os

load_dotenv()

def search_query(query):
    # Load embedding model
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Load existing vector DB
    vector_db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    # Search similar chunks
    results = vector_db.similarity_search(query, k=3)  # Get top 5 similar chunks
    
    # Print results
    for i, result in enumerate(results):
    
        print(f"\nResult {i+1}:\n")
        print(result.page_content)


if __name__ == "__main__":
    search_query("What are the risks mentioned by the company?")
