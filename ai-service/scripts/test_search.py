import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.search_service import semantic_search


def test_search():
    query = "What is revenue growth?"

    results = semantic_search(query, top_k=5)

    print("\nResults:\n")

    for r in results:
        print("Text:", r["text"][:200], "..." if len(r["text"]) > 200 else "")
        print("Metadata:", r.get("metadata"))
        print("-" * 50)

if __name__ == "__main__":
    test_search()
