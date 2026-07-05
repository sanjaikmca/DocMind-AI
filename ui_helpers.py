import streamlit as st


def show_user_message(message):
    with st.chat_message("user"):
        st.markdown(message)


def show_assistant_message(message):
    with st.chat_message("assistant"):
        st.markdown(message)


def add_message(role, content):
    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )