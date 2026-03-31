import os
from dotenv import load_dotenv

# --------------------
# ENV SETUP
# --------------------
load_dotenv()

# Import embedding model from OpenAI
# This converts text into numbers (vectors)
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Import Chroma vector database
# This stores and searches embeddings
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import (
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)

# Import our chunking function
from services.text_chunker import split_text_into_chunks
from services.document_loader import load_pdf

# def get_vector_store():
#     print("--- Starting Ingestion ---")

#     # Step 1: Load PDF
#     pdf_path = "../data/dodla_dairy_annual_report_2025.pdf"
#     text = load_pdf(pdf_path)
#     print(f"Loaded {len(text)} documents.")

#     # Step 2: Split into chunks
#     chunks = split_text_into_chunks(text)
#     print(f"Split into {len(chunks)} chunks.")

#     # Step 3: Create embedding model
#     # embeddings = OpenAIEmbeddings()
#     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#     # Step 4: Store chunks in vector DB
#     # This converts chunks into vectors and saves them in a local directory called "db"
#     vector_db = Chroma.from_texts(
#         texts=chunks, 
#         embedding=embeddings,
#         persist_directory="db"
#     )

# if __name__ == "__main__":
#     get_vector_store()


def get_vector_store():
    """
    Initialize or load the vector database.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_db = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    return vector_db