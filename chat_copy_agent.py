import os
import streamlit as st
from shadai.core.session import Session

st.title("Shadai Chat")

input_dir = os.path.join(os.path.dirname(__file__), "documents")

agent_copy_prompt = """
You are a helpful assistant that can hep to refine marketing copy.
"""

session = Session(type="light")

# Initialize local UI chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if input_user := st.chat_input("Write a marketing copy for a new product"):
    with st.chat_message("user"):
        st.markdown(input_user)
    
    result = session.chat(
        message=input_user,
        system_prompt=agent_copy_prompt
    )
    
    with st.chat_message("assistant"):
        st.markdown(result)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": input_user})
    st.session_state.messages.append({"role": "assistant", "content": result})
    
if file := st.file_uploader("Upload a file"):
    save_path = os.path.join(os.path.dirname(__file__), "documents", file.name)
    with open(save_path, "wb") as f:
        f.write(file.getbuffer())
    with st.chat_message("user"):
        st.markdown(file)
    try:
        session.ingest(
            input_dir=input_dir
        )
        st.markdown("File ingested successfully")
    except Exception as e:
        st.error(e)
        st.error("Error ingesting file")