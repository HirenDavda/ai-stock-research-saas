# Import the text splitter from LangChain
# This tool helps break large text into smaller pieces
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import our PDF loader function
from document_loader import load_pdf

# Function to split text into chunks
def split_text_into_chunks(text):
    # Remove extra spaces and new lines
    text = text.replace("\n", " ").strip()

    # Create a text splitter object
    # chunk_size = maximum characters in one chunk
    # chunk_overlap = small overlap between chunks to keep context
    # Bigger chunks for financial documents
    # This keeps more context like full paragraphs
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000, # Larger chunk = more meaning in one piece
        chunk_overlap = 300 # Keep overlap for continuity
    )

    # Split the full text into smaller chunks
    chunks = text_splitter.split_text(text)

    return chunks

if __name__ == "__main__":

    # Path to your annual report
    pdf_file_path = "../data/dodla_dairy_annual_report_2025.pdf"

    # Load text from the PDF
    document_text = load_pdf(pdf_file_path)

    # Split the text into chunks
    document_chunks = split_chunk_text_into_chunks(document_text)

    # Print number of chunks created
    print(f"Total chunks created: {len(document_chunks)}")

    # Print first chunk for testing
    print("\nFirst Chunk:\n")
    print(document_chunks[0])

    # Save chunks to a text file for inspection
    with open("chunks_output.txt", "w") as f:
        for chunk in document_chunks:
            f.write(chunk)
            f.write("\n---\n")  # Separator between chunks  