# 🧠 DocMind AI

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-orange)
![Ollama](https://img.shields.io/badge/Ollama-Llama%203-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

### Intelligent Document Question Answering System using RAG, Llama 3, LangChain and FAISS

DocMind AI is an AI-powered document question answering system that enables users to upload documents, ask questions in natural language, and receive context-aware answers. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generates accurate responses using Llama 3.

> **Current supported document format:** PDF

---

# ✨ Features

- 📄 Upload one or more documents (PDF support)
- 🤖 Ask questions in natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using FAISS Vector Store
- 💬 Llama 3 powered answer generation
- 📑 Document preview
- 📚 Source citations with page numbers
- 📌 Retrieved context viewer
- 📊 Document statistics
- 🎨 Clean and interactive Streamlit interface
- ⚡ Local and privacy-friendly inference using Ollama

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI Framework | Streamlit |
| LLM | Llama 3 (Ollama) |
| RAG Framework | LangChain |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Store | FAISS |
| Document Processing | PyMuPDF, LangChain Document Loaders |

---

# 🏗 System Architecture

```text
Documents
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
     │
     ▼
Sentence Transformer Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Relevant Context Retrieval
     │
     ▼
Llama 3 (Ollama)
     │
     ▼
Generated Answer + Source Citations
```

---

# 📂 Project Structure

```text
DocMind-AI/
│
├── app.py
├── chatbot.py
├── config.py
├── document_processor.py
├── document_viewer.py
├── loader.py
├── splitter.py
├── embeddings.py
├── vector_store.py
├── ui_helpers.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/sanjaikmca/DocMind-AI.git
```

## Navigate to the project

```bash
cd DocMind-AI
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start Ollama

Make sure Ollama is installed, then run:

```bash
ollama run llama3
```

## Launch the application

```bash
streamlit run app.py
```

---

# 💡 How to Use

1. Launch the application.
2. Upload one or more supported documents (PDF).
3. Wait for document processing to complete.
4. Ask questions about the uploaded content.
5. View the generated answer along with source citations and retrieved context.

---

# 📸 Screenshots

## Home

> *(Add Home Screenshot Here)*

---

## Document Upload

> *(Add Upload Screenshot Here)*

---

## Question Answering

> *(Add Chat Screenshot Here)*

---

## Retrieved Context

> *(Add Retrieved Context Screenshot Here)*

---

## Source Citations

> *(Add Source Citation Screenshot Here)*

---

# 🎯 Project Highlights

- Modular project architecture
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- FAISS semantic search
- Context-aware responses
- Multiple document support
- Source attribution
- Interactive Streamlit interface

---

# 🔮 Future Improvements

- Support additional document formats (DOCX, TXT, Markdown)
- Hybrid Search (BM25 + FAISS)
- Conversation memory
- Document summarization
- Multi-model support
- Streaming LLM responses
- Cloud deployment
- Authentication and user sessions
- Chat history export

---

# 👨‍💻 Developer

## Sanjai K

AI / Machine Learning Engineer

- 🎓 MCA Graduate
- 📄 IEEE Published Researcher

### GitHub

https://github.com/sanjaikmca

### LinkedIn

https://www.linkedin.com/in/sanjaikmca

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
