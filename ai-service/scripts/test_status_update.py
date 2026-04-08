from database.mongo import (
    save_document_metadata,
    update_document_status,
    connect_to_mongo,
    close_mongo_connection,
    STATUS_PROCESSING,
    STATUS_COMPLETED
)

def test_status():

    connect_to_mongo()

    doc_id = save_document_metadata(
        filename="dodla_dairy_annual_report_2025.pdf",
        file_path="../data/dodla_dairy_annual_report_2025.pdf",
        chunks=10,
        file_size=12345,
        content_type="application/pdf"
    )

    update_document_status(
        doc_id,
        STATUS_PROCESSING
    )

    update_document_status(
        doc_id,
        STATUS_COMPLETED
    )

    close_mongo_connection()

if __name__ == "__main__":
    test_status()
