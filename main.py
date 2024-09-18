import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

# URL for the backend API
url = "https://contractors-backend.vercel.app/query"
    
def main():
    st.title("💬 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        data = {
        "query": prompt
        }
        response = requests.post(url, json = data, headers={"Content-Type": "application/json", "Authorization": AUTH_TOKEN})
        msg = response.json()
        print(msg)
        msg_text = msg["results"]
        print(msg_text)
        st.session_state.messages.append({"role": "assistant", "content": msg_text})
        st.chat_message("assistant").write(msg_text)
    
if __name__ == "__main__":
    main()