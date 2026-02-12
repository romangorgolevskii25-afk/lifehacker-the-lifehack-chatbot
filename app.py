
import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="LifeHack Bot",
    page_icon="💡",
    layout="centered"
)

# Custom CSS for cool UI
st.markdown("""
<style>
.chat-box {
    background-color: #f5f7fa;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user {
    background-color: #d1e7ff;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
.bot {
    background-color: #e2ffe6;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💡 LifeHack Chatbot")
st.write("Ask for quick life hacks to make your day easier!")

# Life hack database
life_hacks = {
    "study": [
        "Use the 25–5 Pomodoro rule: study 25 minutes, break 5 minutes.",
        "Teach what you learn to someone else to remember it better.",
        "Study difficult topics right before sleeping."
    ],
    "productivity": [
        "Write tomorrow’s to-do list before sleeping.",
        "Do the hardest task first thing in the morning.",
        "Turn off notifications while working."
    ],
    "health": [
        "Drink a glass of water right after waking up.",
        "Walk for 5 minutes after every hour of sitting.",
        "Sleep and wake up at the same time daily."
    ],
    "general": [
        "Keep your phone in grayscale to reduce scrolling.",
        "Prepare clothes the night before.",
        "Use the 2-minute rule: if it takes <2 min, do it now."
    ]
}

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"
    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your message:")

if st.button("Send 🚀") and user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Simple intent detection
    key = "general"
    for topic in life_hacks:
        if topic in user_input.lower():
            key = topic
            break

    bot_reply = random.choice(life_hacks[key])

    # Save bot message
    st.session_state.messages.append({
        "role": "bot",
        "content": f"💡 {bot_reply}"
    })

    st.experimental_rerun()

import streamlit as st
import random

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="LifeHack Chatbot", page_icon="💡")

# -------------------------
# Title
# -------------------------
st.title("💡 LifeHack Chatbot")
st.write("Ask for quick life hacks to make your day easier!")

# -------------------------
# Life hack database
# -------------------------
life_hacks = {
    "study": [
        "Use the 25–5 Pomodoro rule: study 25 minutes, break 5 minutes.",
        "Teach what you learn to someone else to remember it better.",
        "Study difficult topics right before sleeping."
    ],
    "productivity": [
        "Write tomorrow’s to-do list before sleeping.",
        "Do the hardest task first thing in the morning.",
        "Turn off notifications while working."
    ],
    "health": [
        "Drink a glass of water right after waking up.",
        "Walk for 5 minutes after every hour of sitting.",
        "Sleep and wake up at the same time daily."
    ],
    "general": [
        "Keep your phone in grayscale to reduce scrolling.",
        "Prepare clothes the night before.",
        "Use the 2-minute rule: if it takes less than 2 minutes, do it now."
    ]
}

# -------------------------
# Function to generate response
# -------------------------
def get_lifehack(user_input):
    user_input = user_input.lower()

    if "study" in user_input:
        return random.choice(life_hacks["study"])
    elif "productivity" in user_input or "work" in user_input:
        return random.choice(life_hacks["productivity"])
    elif "health" in user_input:
        return random.choice(life_hacks["health"])
    else:
        return random.choice(life_hacks["general"])

# -------------------------
# Session state for chat
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Display chat history
# -------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat input
# -------------------------
if prompt := st.chat_input("Ask me for a life hack..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    response = get_lifehack(prompt)

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)

