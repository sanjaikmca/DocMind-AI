from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from utils.config import MODEL_NAME


def get_llm():
    """
    Load the Ollama LLM.
    """
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0
    )


def generate_answer(
    llm,
    retrieved_docs,
    question,
    chat_history=""
):
    """
    Generate an answer using the retrieved context.
    """

    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an intelligent AI assistant.

Answer ONLY using the provided context.

Rules:
- If the answer is not available in the context, say:
  "I couldn't find that information in the uploaded documents."
- Do not make up information.
- Keep answers concise and well formatted.
- Use bullet points when appropriate.

Context:
{context}

Conversation History:
{chat_history}

Question:
{question}

Answer:
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "chat_history": chat_history,
            "question": question
        }
    )

    return response.content


def stream_answer(answer):
    """
    Stream answer word by word.
    """

    for word in answer.split():
        yield word + " "