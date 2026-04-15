class BaseVectorStore:
    def add(self, chunks, embeddings, ids, metadata=None):
        raise NotImplementedError

    def search(self, query_embedding, top_k=5):
        raise NotImplementedError    