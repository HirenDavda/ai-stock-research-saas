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
        generate_embeddings_batch
    )
else:
    from services.local_embedding_service import (
        generate_embedding,
        generate_embeddings_batch
    )

