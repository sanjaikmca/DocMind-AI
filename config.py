"""
Application Configuration
"""

# Ollama Model
MODEL_NAME = "llama3"

# Hugging Face Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Vector Database
VECTOR_DB_PATH = "vector_db"

# Text Splitter
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 3