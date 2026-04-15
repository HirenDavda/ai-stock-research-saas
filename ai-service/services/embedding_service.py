import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER",
    "local"
)

print("Embedding provider:", EMBEDDING_PROVIDER)

if EMBEDDING_PROVIDER == "openai":
    from services.openai_embedding_service import (
        generate_embedding,
        generate_embeddings_batch,
    )

    def get_embedding_model():
        raise RuntimeError(
            "get_embedding_model() is only available when EMBEDDING_PROVIDER=local "
            "(SentenceTransformer). Chroma ingest paths expect the local model."
        )
else:
    from services.local_embedding_service import (
        generate_embedding,
        generate_embeddings_batch,
        get_embedding_model,
    )


def get_embedding(text):
    return generate_embedding(text)
