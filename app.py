
import os
import streamlit as st

from utils.embeddings import get_embedding_model
from utils.chatbot import get_llm, generate_answer, stream_answer
from utils.vector_store import load_vector_store, vector_store_exists, search_vector_store
from utils.document_processor import process_documents
from utils.document_viewer import preview_document

st.set_page_config(page_title="DocMind AI", page_icon="🧠", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages=[]

@st.cache_resource
def load_models():
    return get_embedding_model(), get_llm()

embedding_model,llm=load_models()

st.title("🧠 DocMind AI")
st.caption("Intelligent Document Assistant powered by Llama 3, LangChain and FAISS.")

st.sidebar.title("📂 Documents")
st.sidebar.markdown("---")

uploaded_files=st.sidebar.file_uploader("Choose Documents",type=["pdf" , "docx" , "txt" , "md"],accept_multiple_files=True)
st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Workspace Status")
if uploaded_files:
    st.sidebar.success("📄 Documents Loaded")
    st.sidebar.success("🧠 Embeddings Ready")
    st.sidebar.success("💬 Chat Ready")
else:
    st.sidebar.info("📂 Upload Document(s) to begin")



file_paths=[]
if uploaded_files:
    os.makedirs("data", exist_ok=True)

    for file in uploaded_files:
        path = os.path.join("data", file.name)
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        file_paths.append(path)

    with st.spinner("📄 Processing documents..."):
        vector_db = process_documents(file_paths)

    st.success("✅ Documents processed successfully!")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages=[]
    st.rerun()
    st.sidebar.markdown("---")

st.sidebar.subheader("🤖 AI Engine")

st.sidebar.success("🧠 Model: Llama 3")
st.sidebar.success("🖥 Framework: Streamlit")
st.sidebar.success("📦 Vector Store: FAISS")
st.sidebar.success("🔍 Embeddings: all-MiniLM-L6-v2")
st.sidebar.success("👨‍💻 Built by Sanjai K")    
left,right=st.columns([1,2])

with left:
    st.subheader("📄 Document Preview")

    if file_paths:

        selected_document = st.selectbox(
            "Select a document",
            file_paths,
            format_func=lambda x: os.path.basename(x)
        )

        preview_document(selected_document)

    else:
        st.info("Upload documents to preview.")

with right:
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            if m.get("sources"):

                st.markdown("#### 📄 Sources")

                for source in m["sources"]:
                    st.markdown(source)
    question=st.chat_input("Ask a question...")

    if question:
        st.session_state.messages.append({"role":"user","content":question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            if vector_store_exists():

                status = st.empty()
                status.info("🧠 Analyzing your documents...")

                vector_db = load_vector_store(embedding_model)

                results = search_vector_store(
                    vector_db,
                    question,
                    k=3
                )

                docs = [doc for doc, score in results]

                history = "\n".join(
                    f"{m['role']}: {m['content']}"
                    for m in st.session_state.messages[-6:]
                )

                answer = generate_answer(
                    llm,
                    docs,
                    question,
                    history
                )

                status.empty()

                shown = st.write_stream(stream_answer(answer))

                st.info(
                    f"Retrieved {len(docs)} relevant document chunk(s)."
                )

                st.divider()

                st.markdown("### 📄 Sources")

                from collections import defaultdict

                source_pages = defaultdict(set)

                for doc in docs:

                    filename = doc.metadata.get(
                        "source_file",
                        "Unknown Document"
                    )

                    page = doc.metadata.get("page", 0) + 1

                    source_pages[filename].add(page)

                sources = []

                for filename, pages in source_pages.items():

                    st.markdown(f"**📘 {filename}**")

                    pages = sorted(pages)

                    for i, page in enumerate(pages):

                        prefix = "└──" if i == len(pages) - 1 else "├──"

                        st.markdown(
                            f"&nbsp;&nbsp;&nbsp;{prefix} Page {page}",
                            unsafe_allow_html=True
                        )

                        sources.append(f"{filename} - Page {page}")

                with st.expander("🔍 Retrieved Context"):

                    for i, (doc, score) in enumerate(results, start=1):

                        st.markdown(f"### Chunk {i}")

                        st.write(
                            f"Document: {doc.metadata.get('source_file', 'Unknown')}"
                        )

                        st.write(
                            f"Page: {doc.metadata.get('page', 0) + 1}"
                        )

                        st.write(doc.page_content[:300] + "...")

                        st.divider()

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": shown,
                        "sources": sources
                    }
                )

            else:

                st.warning("Please upload document(s) first.")
st.divider()

st.markdown("""
**Developed by Sanjai K | AI/ML Engineer**

📄 IEEE Published Researcher

🔗 **GitHub:** [github.com/sanjaikmca](https://github.com/sanjaikmca)

🔗 **LinkedIn:** [linkedin.com/in/sanjaikmca](https://www.linkedin.com/in/sanjaikmca)
""")
