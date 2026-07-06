from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)


def load_document(file_path):
    """
    Loads PDF, DOCX, TXT, or Markdown files
    and returns LangChain Document objects.
    """

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)

    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")

    elif file_path.endswith(".md"):
        loader = TextLoader(file_path, encoding="utf-8")

    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    documents = loader.load()

    return documents
