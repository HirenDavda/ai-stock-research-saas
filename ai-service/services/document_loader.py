# Import the PDF reader library
# This library helps us read text from PDF files
from pathlib import Path
from pypdf import PdfReader
import docx

# This function reads a PDF file
# and returns all text inside the document
def load_document(file_path: str) -> str:
    """
    Load document content based on file type
    """

    print("Loading document:", file_path)

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf(file_path)
    elif suffix == ".txt":  
        return load_text(file_path)
    elif suffix == ".docx":
        return load_docx(file_path)            
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def load_pdf(file_path: str) -> str:
    print("Reading PDF")

    # Open a PDF file reader object using the provided file path
    reader = PdfReader(file_path)

    # Create empty string to store text from the PDF
    text = []

    # Loop through each and every page in the PDF
    for page in reader.pages:
        content = page.extract_text()

        # Add that text to the full document text
        if content:
            text.append(content)

    # Return the complete document text from the PDF
    return "\n".join(text)


def load_text(file_path: str) -> str:
    print("Reading TXT")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_docx(file_path: str) -> str:
    print("Reading DOCX")

    document = docx.Document(file_path)

    paragraphs = []

    for p in document.paragraphs:
        paragraphs.append(p.text)

    return "\n".join(paragraphs) 

# # Run this code only if this file is executed directly
# if __name__ == "__main__":
#     # Location of the PDF file to read
#     pdf_file_path = "data/dodla_dairy_annual_report_2025.pdf"

#     # Call the function to read the PDF and get the text
#     document_text = load_document(pdf_file_path)

#     # Print first 1000 characters of the extracted text
#     # This helps us check if text extraction worked correctly
#     print(document_text[:1000])