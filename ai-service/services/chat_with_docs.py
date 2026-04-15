import os
from dotenv import load_dotenv

from database.chroma_client import collection
from langchain_google_genai import ChatGoogleGenerativeAI

from config import RAG_TOP_K
from services.embedding_service import get_embedding

TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))

load_dotenv()


def ask_question(question):
    """
    Retrieve chunks via the same raw Chroma collection used for ingest
    (database.chroma_client) and answer with the LLM.
    """
    # Step 1: Default answer and sources when retrieval returns nothing
    answer = "Not found in document"
    sources = []

    # Step 2: Embed the user question (same embedding path as ingest / search_service)
    query_embedding = get_embedding(question)

    # Step 3: Query Chroma for the most similar stored chunks
    raw = collection.query(
        query_embeddings=[query_embedding],
        n_results=max(1, RAG_TOP_K),
        include=["documents", "metadatas"],
    )

    docs = raw.get("documents", [[]])[0] or []
    metas = raw.get("metadatas", [[]])[0] or []

    # Step 4: Exit with defaults if nothing matched; else merge chunk text into context
    if not docs:
        return {"answer": answer, "sources": sources}

    context = "\n\n".join(docs)

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

    # Step 6: Create LLM (Gemini) that will draft the answer from the prompt
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

    llm = ChatGoogleGenerativeAI(
        model = MODEL_NAME,
        temperature = TEMPERATURE
    )

    # Step 7: Generate answer
    response = llm.invoke(prompt)

    # Step 8: Print sources and answer (helpful when running as a script)
    print("\nSources:\n")

    for i, doc in enumerate(docs):
        print(f"Source {i+1}:\n")
        print(doc[:300])

    print("\nAI Answer:\n")
    print(response.content)

    # Step 9: Shape structured sources for API / callers
    sources = [
        {"text": doc[:500], "metadata": meta if meta is not None else {}}
        for doc, meta in zip(docs, metas)
    ]

    # Step 10: Return answer text and source snippets + metadata
    return {
        "answer": response.content,
        "sources": sources,
    }


if __name__ == "__main__":
    ask_question("Revenue?")
