import os
from .settings import DATA_DIR
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

INDEX_DIR = os.path.join(DATA_DIR, ".index")

def _ensure_index() -> VectorStoreIndex:
    if os.path.isdir(INDEX_DIR):
        storage = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage)
    docs = SimpleDirectoryReader(DATA_DIR, recursive=True, required_exts=[".md",".txt"]).load_data()
    idx = VectorStoreIndex.from_documents(docs)
    idx.storage_context.persist(persist_dir=INDEX_DIR)
    return idx

def query_docs(q: str) -> str:
    idx = _ensure_index()
    return idx.as_query_engine().query(q).response.strip()
