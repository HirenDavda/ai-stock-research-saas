# Import the PDF reader library
# This library helps us read text from PDF files
from pypdf import PdfReader

# This function reads a PDF file
# and returns all text inside the document
def load_pdf(file_path):
    # Open a PDF file reader object using the provided file path
    reader = PdfReader(file_path)
    
    # Create empty string to store text from the PDF
    full_text = ""
    
    # Loop through each and every page in the PDF
    for page in reader.pages:
        # Extract text from that page
        page_text = page.extract_text()

        # Add that text to the full document text
        full_text += page_text
    
    # Return the complete document text from the PDF
    return full_text


# Run this code only if this file is executed directly
if __name__ == "__main__":
    # Location of the PDF file to read
    pdf_file_path = "data/dodla_dairy_annual_report_2025.pdf"

    # Call the function to read the PDF and get the text
    document_text = load_pdf(pdf_file_path)

    # Print first 1000 characters of the extracted text
    # This helps us check if text extraction worked correctly
    print(document_text[:1000])