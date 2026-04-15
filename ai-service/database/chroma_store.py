class ChromaStore:
    def add(self, chunks, embeddings, ids, metadata=None):
        return self.add_chunks(chunks, embedding, ids, metadata)

    def search(self, query_embedding, top_k=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )    