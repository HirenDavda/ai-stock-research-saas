from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_document(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
):
    """
    Split document text into chunks
    """

    print("Starting document chunking...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    print("Chunks created:", len(chunks))

    return chunks


