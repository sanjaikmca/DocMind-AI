import os
from langchain_community.vectorstores import FAISS


VECTOR_DB_PATH = "vector_db"


def create_vector_store(chunks, embedding_model):
    """
    Create a FAISS vector store from document chunks.
    """

    if len(chunks) == 0:
        raise ValueError("No chunks found to create the vector database.")

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_db


def save_vector_store(vector_db):
    """
    Save FAISS vector database.
    """

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    vector_db.save_local(VECTOR_DB_PATH)


def load_vector_store(embedding_model):
    """
    Load FAISS vector database.
    """

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )


def vector_store_exists():
    """
    Check whether FAISS database exists.
    """

    return (
        os.path.exists(
            os.path.join(VECTOR_DB_PATH, "index.faiss")
        )
        and
        os.path.exists(
            os.path.join(VECTOR_DB_PATH, "index.pkl")
        )
    )

def search_vector_store(vector_db, query, k=4):
    """
    Retrieve the top-k most relevant chunks.
    """

    return vector_db.similarity_search_with_score(
        query,
        k=k
    )