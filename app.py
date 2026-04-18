import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="GenAI Chatbot", layout="centered")

st.title("🤖 GenAI Chatbot")
st.write("Simple chatbot using OpenAI / Groq")

# Sidebar
provider = st.sidebar.selectbox("Select Provider", ["OpenAI", "Groq"])

model = st.sidebar.selectbox("Select Model", [
    "gpt-3.5-turbo",
    "llama3-70b-8192"
])

system_prompt = st.sidebar.text_area(
    "System Prompt",
    "You are a helpful assistant"
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Dummy response (SAFE for deployment)
    response = f"🤖 Answer: {user_input}"

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)