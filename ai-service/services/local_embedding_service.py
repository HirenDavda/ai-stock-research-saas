from typing import Optional

from sentence_transformers import SentenceTransformer

_MODEL_NAME = "all-MiniLM-L6-v2"
_model: Optional[SentenceTransformer] = None


def get_embedding_model() -> SentenceTransformer:
    """Single shared SentenceTransformer instance (lazy-loaded)."""
    global _model
    if _model is None:
        print("Loading local embedding model...")
        _model = SentenceTransformer(_MODEL_NAME)
        print("Local model loaded")
    return _model


def generate_embedding(text: str):
    return get_embedding_model().encode(text).tolist()


def generate_embeddings_batch(chunks):
    embeddings = get_embedding_model().encode(chunks)
    return [vector.tolist() for vector in embeddings]
