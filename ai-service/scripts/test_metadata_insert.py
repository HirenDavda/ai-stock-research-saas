# scripts/test_metadata_insert.py
from database.mongo import connect_to_mongo, save_document_metadata
from dotenv import load_dotenv

def test_insert():
    # STEP 1 — Connect to MongoDB
    print("Connecting now...")
    connect_to_mongo()
    print("Connection attempted")

    # STEP 2 — Insert metadata
    # document_data = {
    #     "document_id": "test_doc_001",
    #     filename = "dodla_dairy_annual_report_2025.pdf",
    #     file_path = "data/dodla_dairy_annual_report_2025.pdf",
    #     chunks = 10,
    #     "file_size": 1024,
    #     "upload_time": "2026-04-03",
    #     "status": "processed"
    # }
    
    # result = save_document_metadata(document_data)

    result = save_document_metadata(
        filename="dodla_dairy_annual_report_2025.pdf",
        file_path="../data/dodla_dairy_annual_report_2025.pdf",
        chunks=10,
        file_size=12345,
        content_type="application/pdf"
    )

    print("Insert Result:", result)


if __name__ == "__main__":
    test_insert()