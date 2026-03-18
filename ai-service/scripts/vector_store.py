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

# Import our chunking function
from text_chunker import split_text_into_chunks
from document_loader import load_pdf

def create_vector_store():
    print("--- Starting Ingestion ---")

    # Step 1: Load PDF
    pdf_path = "../data/dodla_dairy_annual_report_2025.pdf"
    text = load_pdf(pdf_path)
    print(f"Loaded {len(text)} documents.")

    # Step 2: Split into chunks
    chunks = split_text_into_chunks(text)
    print(f"Split into {len(chunks)} chunks.")

    # Step 3: Create embedding model
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Step 4: Store chunks in vector DB
    # This converts chunks into vectors and saves them in a local directory called "db"
    vector_db = Chroma.from_texts(
        texts=chunks, 
        embedding=embeddings,
        persist_directory="db"
    )

if __name__ == "__main__":
    create_vector_store()
