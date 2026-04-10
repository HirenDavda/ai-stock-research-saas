from database.vector_store import (
    save_document_chunks,
    create_indexes
)

def test_vector_store():

    

    document_id = "test_doc_001"

    chunks = [
        "Revenue increased by 15%",
        "Operating margin improved"
    ]

    embeddings = [
        [0.1] * 384,
        [0.2] * 384
    ]

    create_indexes()

    ids = save_document_chunks(
        document_id,
        chunks,
        embeddings
    )
    
    print("Inserted IDs:", ids) 

if __name__ == "__main__":
    test_vector_store()


