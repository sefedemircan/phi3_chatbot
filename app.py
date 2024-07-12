from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="phi3")

st.title("PHI3 Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Prompt: "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("Llama3"):
        response = llm.stream(prompt, stop=["<|eot_id|>]"])
        st.write(response)
        st.session_state.messages.append({"role": "PHI3", "content": response})