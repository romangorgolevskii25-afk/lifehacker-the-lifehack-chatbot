import streamlit as st

# Page setup
st.set_page_config(
    page_title="Lifehacker Chatbot 🐱",
    page_icon="🐱"
)

st.title("🐱 Lifehacker Chatbot")
st.write("Ask me for a lifehack and I’ll help you out!")

# Simple lifehack responses
def catbot_response(user_input):
    user_input = user_input.lower()

    if "study" in user_input:
        return "🐱 Try the 25-minute Pomodoro method! Study hard, then nap like a cat 😴"
    elif "sleep" in user_input:
        return "🐱 No screens 1 hour before bed. Cats approve of naps 💤"
    elif "stress" in user_input:
        return "🐱 Take 5 deep breaths. If stressed, stretch like a cat 🧘‍♂️"
    elif "clean" in user_input:
        return "🐱 Clean for just 10 minutes. Small wins = big purrs 😸"
    else:
        return "🐱 Interesting! My lifehack: break big problems into tiny cat-sized steps."

# Input box
user_input = st.text_input("💬 Your question:")

if user_input:
    response = catbot_response(user_input)
    st.success(response)
