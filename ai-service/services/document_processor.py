# from services.document_chunker import chunk_document
# from services.document_loader import load_document
# from services.embedding_service import generate_embeddings_batch

from services import (
    load_document,
    chunk_document,
    generate_embeddings_batch
)

from database.mongo import (
    update_document_status,
    STATUS_PROCESSING,
    STATUS_COMPLETED,
    STATUS_FAILED
)

from database.vector_store import save_document_chunks

def process_document(document_id: str):
    """
    Main document processing pipeline
    """

    print("Starting document processing:", document_id)

    try: 
        # Step 1 — mark processing
        update_document_status(
            document_id,
            STATUS_PROCESSING
        ) 

        print("Step 1 — Processing started")

        # Step 2 — Simulate document text (temporary)
        print("Step 2 — Chunking document")
        text = load_document(file_path)

         # Step 3 — Chunk document
        print("Step 3 — Chunking document")
        chunks = chunk_document(text)
        print("Chunk count:", len(chunks))

        # Step 4 — placeholder for embeddings
        print("Step 4 — Generating embeddings")
        embeddings = generate_embeddings_batch(chunks)
        print("Embeddings created:", len(embeddings))

        print("Storing vectors...")
        save_document_chunks(
            document_id=document_id,
            chunks=chunks,
            embeddings=embeddings
        )


        # Step 5 — mark completed
        update_document_status(
            document_id,
            STATUS_COMPLETED
        )
        print("Document processing completed")

    except Exception as e:
        print("Processing failed:", str(e))

        update_document_status(
            document_id,
            STATUS_FAILED,
            error=str(e)
        )    