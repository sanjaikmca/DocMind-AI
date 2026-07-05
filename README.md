# 🧠 DocMind AI

### Intelligent Document Question Answering System using RAG, Llama 3, LangChain and FAISS

DocMind AI is an AI-powered document question answering system that allows users to upload one or more PDF documents and ask questions in natural language. The application retrieves the most relevant information from the uploaded documents using Retrieval-Augmented Generation (RAG) and generates accurate answers using Llama 3.

---

## 🚀 Features

- 📄 Upload multiple PDF documents
- 🔍 Semantic document search using FAISS
- 🤖 Llama 3 powered question answering
- 🧠 SentenceTransformer embeddings
- 📑 PDF preview
- 📚 Source citation with page numbers
- 📌 Retrieved context viewer
- 📊 Document statistics
- 💬 Interactive chat interface
- 🌙 Clean Streamlit UI

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| LLM | Llama 3 (Ollama) |
| RAG Framework | LangChain |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| PDF Processing | PyMuPDF, PyPDFLoader |

---

## 📂 Project Structure

```text
DocMind-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── config.py
│
├── chatbot.py
├── document_processor.py
├── document_viewer.py
├── loader.py
├── splitter.py
├── embeddings.py
├── vector_store.py
├── ui_helpers.py
│
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/sanjaikmca/DocMind-AI.git
```

Go to the project directory

```bash
cd DocMind-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama run llama3
```

Run the application

```bash
streamlit run app.py
```

---

## 📖 How to Use

1. Launch the application.
2. Upload one or more PDF documents.
3. Wait until document processing is complete.
4. Ask questions related to the uploaded documents.
5. View retrieved sources and supporting context.

---

## 📸 Screenshots

### Home Page

> *(Add screenshot here)*

### Upload Documents

> *(Add screenshot here)*

### Chat Response

> *(Add screenshot here)*

### Retrieved Context

> *(Add screenshot here)*

---

## 🔮 Future Improvements

- Conversation memory
- Hybrid Search (BM25 + FAISS)
- Document summarization
- Citation highlighting
- Multiple LLM support
- Cloud deployment
- User authentication

---

## 👨‍💻 Developer

**Sanjai K**

AI / Machine Learning Engineer

- 🔗 GitHub: https://github.com/sanjaikmca
- 🔗 LinkedIn: https://www.linkedin.com/in/sanjaikmca

---

## 📄 License

This project is licensed under the MIT License.
