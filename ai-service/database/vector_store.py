from datetime import datetime
from database.mongo import get_database

COLLECTION_NAME = "document_chunks"

def get_chunks_collection():

    db = get_database()

    return db[COLLECTION_NAME]

def save_document_chunks(
    document_id: str,
    chunks: list,
    embeddings: list
):
    """
    Store chunks and embeddings in MongoDB
    """
    
    collection = get_chunks_collection()

    records = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        record = {
            "document_id": document_id,
            "chunk_index": index,
            "text": chunk,
            "embedding": embedding,
            "created_at": datetime.utcnow()
        }

        records.append(record)

    result = collection.insert_many(records)

    print(
        "Chunks stored:",
        len(result.inserted_ids)
    )

    return result.inserted_ids


def create_indexes():

    collection = get_chunks_collection()

    collection.create_index(
        [("document_id", 1)]
    )    

    collection.create_index(
        [("chunk_index", 1)]
    )

    print("Indexes created")