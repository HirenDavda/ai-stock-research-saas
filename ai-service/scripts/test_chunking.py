from services.document_chunker import chunk_document

def test_chunking():

    sample_text = """
    Artificial Intelligence is transforming industries.

    Companies use AI to analyze financial reports,
    automate research, and improve decision making.

    Investors rely on AI systems to process large
    volumes of documents quickly.
    """ * 50

    chunks = chunk_document(sample_text)

    print("Total chunks:", len(chunks))

    print("\nFirst chunk preview:\n")
    print(chunks[0][:300])

if __name__ == "__main__":
    test_chunking()    