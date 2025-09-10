import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDVu2YYYhgqRLba-RtZf54Arn_e-9yVXq0")

# --- Initialize chat session in Streamlit state ---
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-1.5-flash")
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your DSA Instructor. How can I help you today?"}
    ]

# --- Streamlit Page Config ---
st.set_page_config(page_title="DSA Instructor", page_icon="🤖",layout="centered",
    initial_sidebar_state="auto",)

st.title("🎓 DSA Instructor Chatbot")
st.caption("Your personal assistant for Data Structures and Algorithms")

# --- Display chat history ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat input ---
if prompt := st.chat_input("Ask your DSA question here..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Send message with history maintained inside chat object
            response = st.session_state.chat.send_message(
                f"You are a DSA instructor. Only answer DSA-related questions. if someone appreciate you take that appreciation humbly."
                f"The user's question is: {prompt}"
            )
            reply = response.text
            st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    # --- How to Run the App ---
st.sidebar.header("How to Run")
st.sidebar.info(
    "1. Click on the bar.\n"
    "2. Write your question you want to ask.\n"
    "3. Click on enter button. and here you go !"
)

st.sidebar.header("About")
st.sidebar.info(
    "This is a simple chatbot interface built with Streamlit for a DSA instructor created by Rajat and gemini model."
)
