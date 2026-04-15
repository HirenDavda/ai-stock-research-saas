import chromadb

# Use PersistentClient so vectors persist across separate Python processes (scripts, REPL, server).
client = chromadb.PersistentClient(
    path="./chroma_db",
    settings=chromadb.config.Settings(anonymized_telemetry=False),
)

# Create or get collection
collection = client.get_or_create_collection(
    name="documents"
)