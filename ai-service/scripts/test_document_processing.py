from database.mongo import (
    connect_to_mongo,
    close_mongo_connection,
    save_document_metadata
)
# Change 'service' to 'services'
from services.document_processor import process_document

def test_processing():

    connect_to_mongo()

    doc_id = save_document_metadata(
        filename="dodla_dairy_annual_report_2025.pdf",
        file_path="../data/dodla_dairy_annual_report_2025.pdf",
        chunks=10,
        file_size=12345,
        content_type="application/pdf"
    )

    process_document(doc_id)

    close_mongo_connection()

if __name__ == "__main__":
    test_processing()

