import os

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma



DATA_PATH = "data"
DB_PATH = "db"


def ingest_documents():

    print("Loading documents...")

    loader = DirectoryLoader(
        DATA_PATH,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Saving to vector database...")

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    print("Ingestion complete")
    print("Database saved to:", DB_PATH)


if __name__ == "__main__":
    ingest_documents()