import os

from utils.loader import load_document
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vector_store import (
    create_vector_store,
    save_vector_store,
)


def process_documents(file_paths):
    """
    Process multiple documents into one FAISS database.
    """

    all_documents = []

    for file_path in file_paths:

        # Load PDF, DOCX, TXT or MD
        documents = load_document(file_path)

        # Save the filename in metadata
        for doc in documents:
            doc.metadata["source_file"] = os.path.basename(file_path)

        all_documents.extend(documents)

    chunks = split_documents(all_documents)

    num_pages = len(all_documents)
    num_chunks = len(chunks)

    embedding_model = get_embedding_model()

    vector_db = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(vector_db)

    return vector_db, num_pages, num_chunks