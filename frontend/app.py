import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# -------------------- SESSION STATE INIT --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# -------------------- TITLE --------------------
st.markdown(
    "<h1 style='text-align:center;'>🤖 AI Chatbot</h1>",
    unsafe_allow_html=True
)

# -------------------- CHAT DISPLAY --------------------
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(
            f"""
            <div style="text-align:right; margin:10px;">
                <span style="
                    background:#0B5ED7;
                    color:white;
                    padding:10px 14px;
                    border-radius:16px;
                    display:inline-block;
                    max-width:70%;
                ">
                    {chat['content']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="text-align:left; margin:10px;">
                <span style="
                    background:#E9ECEF;
                    color:black;
                    padding:10px 14px;
                    border-radius:16px;
                    display:inline-block;
                    max-width:70%;
                ">
                    {chat['content']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------- BACKEND CALL --------------------
def get_bot_response(message):
    try:
        res = requests.post(
            "https://sufyan-ai-chatbot.onrender.com",
            json={"message": message},
            timeout=30
        )
        return res.json().get("reply", "No response")
    except Exception as e:
        return f"Error: {e}"

# -------------------- INPUT FORM (ENTER = SEND) --------------------
with st.form(key="chat_form", clear_on_submit=True):
    user_message = st.text_input(
        "Type your message...",
        value=st.session_state.user_input
    )

    send_clicked = st.form_submit_button("Send")

# -------------------- HANDLE SEND --------------------
if send_clicked and user_message.strip():
    # User msg
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_message
    })

    # Bot reply
    with st.spinner("🤖 Thinking..."):
        bot_reply = get_bot_response(user_message)

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": bot_reply
    })

    st.session_state.user_input = ""
    st.rerun()

# -------------------- CLEAR CHAT --------------------
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.user_input = ""
    st.rerun()