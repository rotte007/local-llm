import streamlit as st
import requests
import json

def query_ollama(prompt, model="gemma3:1b"):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("message", {}).get("content", "")

st.title("Gemma 3 LLM Chat (Ollama)")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Model:** {msg['bot']}")

prompt = st.text_input("Enter your message:", "")
if st.button("Send") and prompt:
    messages = [{"role": "user", "content": m["user"]} for m in st.session_state["messages"]]
    messages.append({"role": "user", "content": prompt})
    response = query_ollama(messages)
    st.session_state["messages"].append({"user": prompt, "bot": response})
    st.rerun()