"""
Semantic Search Service

Responsibilities:
- Convert query to embedding
- Perform vector similarity search
- Return top relevant chunks
"""

# from database.mongo import collection
# from database.mongo import get_document_collection
# from services.embedding_service import generate_embedding

from database.chroma_client import collection
from services.embedding_service import get_embedding

def semantic_search(query, top_k=5):
    """
    Perform semantic search using ChromaDB
    """

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    output = []

    for doc, meta in zip(documents, metadatas):
        output.append({
            "text": doc,
            "metadata": meta
        })

    return output

# def semantic_search(
#     query: str,
#     top_k: int = 5
# ):

#     """
#     Perform semantic vector search.

#     Args:
#         query (str): User question
#         top_k (int): Number of results

#     Returns:
#         List of relevant document chunks
#     """

#     print("Generating query embedding...")

#     query_embedding = generate_embedding(query)

#     print("Searching vector database...")

#     pipeline = [
#         {
#             "$vectorSearch": {
#                 "index": "vector_index",
#                 "path": "embedding",
#                 "queryVector": query_embedding,
#                 "numCandidates": 100,
#                 "limit": top_k
#             }
#         },
#         {
#             "$project": {
#                 "text": 1,
#                 "source": 1,
#                 "page": 1,
#                 "score": {
#                     "$meta": "vectorSearchScore"
#                 }
#             }
#         }
#     ]

#     collection = get_document_collection()

#     results = list(collection.aggregate(pipeline))

#     print(f"Found {len(results)} results") 

#     return results