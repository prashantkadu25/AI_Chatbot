import time
import streamlit as st
from utils.gemini import create_chat

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.caption("Powered by Google Gemini")

# ---------------------------------------------------
# Session State
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = create_chat()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:

    st.header("🤖 AI Assistant")

    st.success("Gemini 2.5 Flash")

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    st.divider()

    if st.button("🆕 New Chat"):

        st.session_state.chat = create_chat()
        st.session_state.messages = []
        st.rerun()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.info("Version 1.0")

# ---------------------------------------------------
# Display Previous Messages
# ---------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    # ---------------- USER MESSAGE ---------------- #

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------- ASSISTANT MESSAGE ---------------- #

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_response = ""

        start_time = time.time()

        try:

            with st.spinner("🤖 Gemini is thinking..."):

                response = st.session_state.chat.send_message(prompt)

                for word in response.text.split():

                    full_response += word + " "

                    placeholder.markdown(full_response + "▌")

                    time.sleep(0.03)

                placeholder.markdown(full_response)

        except Exception as e:

            full_response = f"❌ Error: {e}"

            placeholder.error(full_response)

        response_time = round(time.time() - start_time, 2)

        st.caption(f"⏱ Response Time : {response_time} sec")

    # Save AI response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )