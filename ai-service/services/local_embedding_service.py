from sentence_transformers import SentenceTransformer

print("Loading local embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Local model loaded")


def generate_embedding(text: str):

    embedding = model.encode(text)

    return embedding.tolist()


def generate_embeddings_batch(chunks):

    embeddings = model.encode(chunks)

    return [vector.tolist() for vector in embeddings]