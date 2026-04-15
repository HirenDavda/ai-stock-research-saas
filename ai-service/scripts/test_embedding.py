import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.embedding_service import generate_embedding


def test_embedding():

    text = "Reliance Industries reported strong revenue growth."

    vector = generate_embedding(text)

    if vector:
        print("Embedding generated")
        print("Vector length:", len(vector))

    else: 
        print("Embedding failed")     

if __name__ == "__main__":
    test_embedding()           