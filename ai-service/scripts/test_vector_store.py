import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from vector_store.factory import get_vector_store
from services.search_service import semantic_search

from database.mongo import connect_to_mongo
from database.vector_store import (
    save_document_chunks,
    create_indexes
)

def test_vector_store():    

    document_id = "test_doc_001"
    connect_to_mongo()

    chunks = [
        "Revenue increased by 15%",
        "Operating margin improved"
    ]

    texts = chunks

    embeddings = [
        [0.1] * 384,
        [0.2] * 384
    ]

    create_indexes()

    ids = save_document_chunks(
        document_id,
        chunks,
        embeddings,
        [{"source": "test", "page": 1}] * len(texts)
    )
    
    print("Inserted IDs:", ids) 

if __name__ == "__main__":
    test_vector_store()


