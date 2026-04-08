from services.document_loader import load_document

def test_loader():
    file_path = "data/sample.txt"

    text = load_document(file_path)

    print("Characters loaded:", len(text))

    print("\nPreview:\n")

    print(text[:500])

if __name__ == "__main__":
    test_loader()    