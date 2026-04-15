from db.chroma_store import ChromaStore
# future:
# from db.mongo_store import MongoStore

def get_vector_store(db_type="chroma"):
    if db_type == "chroma":
        return ChromaStore()

    # if db_type == "mongo":
    #     return MongoStore()

    raise ValueError(f"Unsupported DB type: {db_type}")