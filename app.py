import streamlit as st
import random
import os

# Optional: OpenAI (only works if you add API key)
USE_AI = False
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_AI = True
except:
    USE_AI = False


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="LifeHack Bot", page_icon="💡")

st.title("💡 Smart LifeHack Bot")
st.write("Ask for useful life hacks tailored to you!")

# -----------------------------
# Memory (Chat History)
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Categories + Hacks
# -----------------------------
lifehacks = {
    "food": [
        "🥑 Store avocados with onions to slow browning.",
        "🍋 Microwave lemons for 10s to get more juice.",
        "🍝 Salt water AFTER it boils to cook faster."
    ],
    "study": [
        "⏱ Use the 25-min Pomodoro technique.",
        "🧠 Teach someone else to remember better.",
        "📵 Put your phone in another room while studying."
    ],
    "money": [
        "💰 Use the 50/30/20 budgeting rule.",
        "🛒 Never shop hungry to avoid overspending.",
        "📉 Cancel subscriptions you don’t use."
    ],
    "sleep": [
        "🌙 Avoid screens 30 min before bed.",
        "❄️ Keep your room cool for better sleep.",
        "📴 Try a consistent sleep schedule."
    ],
    "general": [
        "💧 Drink water before meals to avoid overeating.",
        "🧹 Do 5-minute cleanups daily.",
        "📅 Plan tomorrow the night before."
    ]
}

# -----------------------------
# Intent Detection
# -----------------------------
def get_category(text):
    text = text.lower()

    if any(word in text for word in ["food", "eat", "cook", "kitchen"]):
        return "food"
    elif any(word in text for word in ["study", "exam", "learn"]):
        return "study"
    elif any(word in text for word in ["money", "save", "budget"]):
        return "money"
    elif any(word in text for word in ["sleep", "tired", "bed"]):
        return "sleep"
    else:
        return "general"


# -----------------------------
# AI Response (Smart Mode)
# -----------------------------
def ai_lifehack(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You give short, practical, clever life hacks."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except:
        return None


# -----------------------------
# Fallback Logic
# -----------------------------
def basic_lifehack(category):
    return random.choice(lifehacks.get(category, lifehacks["general"]))


# -----------------------------
# UI Buttons (Quick Access)
# -----------------------------
st.subheader("🔥 Quick Categories")

col1, col2, col3, col4 = st.columns(4)

if col1.button("🍔 Food"):
    user_input = "food hacks"
elif col2.button("📚 Study"):
    user_input = "study hacks"
elif col3.button("💰 Money"):
    user_input = "money hacks"
elif col4.button("😴 Sleep"):
    user_input = "sleep hacks"
else:
    user_input = st.text_input("Ask me for a life hack...")


# -----------------------------
# Process Input
# -----------------------------
if user_input:
    st.session_state.history.append(user_input)

    category = get_category(user_input)

    # Try AI first
    if USE_AI:
        reply = ai_lifehack(user_input)
    else:
        reply = None

    # Fallback if AI not available
    if not reply:
        reply = basic_lifehack(category)

    st.session_state.history.append(reply)


# -----------------------------
# Display Chat
# -----------------------------
st.subheader("💬 Chat")

for i in range(0, len(st.session_state.history), 2):
    if i < len(st.session_state.history):
        st.markdown(f"**🧑 You:** {st.session_state.history[i]}")
    if i+1 < len(st.session_state.history):
        st.markdown(f"**💡 Bot:** {st.session_state.history[i+1]}")


# -----------------------------
# Smart Follow-Up
# -----------------------------
if st.session_state.history:
    st.write("👉 Try asking: 'cheap food hacks', 'focus better', 'save money fast'")
