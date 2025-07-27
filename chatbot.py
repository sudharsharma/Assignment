import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
key = os.getenv("GROQ_API_KEY")
if not key:
    st.error("❗ Missing GROQ_API_KEY"); st.stop()

client = Groq(api_key=key)
st.title("Chat")

if "msgs" not in st.session_state:
    st.session_state.msgs = [{"role": "system", "content": "You are helpful."}]

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Say something"):
    st.session_state.msgs.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = client.chat.completions.create(
                    model="llama3‑70b‑8192",
                    messages=st.session_state.msgs
                )
                reply = res.choices[0].message.content
            except Exception as e:
                reply = f"Error: {e}"
        st.markdown(reply)
    st.session_state.msgs.append({"role": "assistant", "content": reply})
