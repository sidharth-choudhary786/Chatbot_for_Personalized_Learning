import streamlit as st
import requests
import json
import time

# Function to fetch response from Rasa
def fetch_response(user_input):
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )
        if response.status_code == 200:
            messages = response.json()
            return [message.get("text", "I didn't understand that.") for message in messages]
        return ["Error: Could not connect to Rasa server."]
    except requests.exceptions.RequestException:
        return ["Error: Rasa server is not running."]

# Streamlit UI Setup
st.set_page_config(page_title="AI Educational Chatbot", layout="wide")
st.title("🤖 AI Educational Chatbot")

# Sidebar - Learning Resources
st.sidebar.header("📚 Learning Resources")
learning_resources = {
    "Rasa Documentation": "https://rasa.com/docs",
    "Streamlit Documentation": "https://docs.streamlit.io",
    "Python Basics": "https://www.w3schools.com/python/",
    "NLP with Python": "https://realpython.com/nltk-nlp-python/",
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Deep Learning": "https://www.deeplearning.ai/",
    "AI Ethics": "https://aiethicslab.com/",
    "Data Science": "https://www.datacamp.com/"
}
for name, url in learning_resources.items():
    st.sidebar.markdown(f"[{name}]({url})")

# Sidebar - Feedback Section
st.sidebar.header("💬 Provide Feedback")
feedback = st.sidebar.text_area("What do you think about the chatbot?")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.success("Thank you for your feedback!")

# Chat History Initialization
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chatbot User Input
st.write("## Ask me anything about education!")
user_input = st.text_input("Type your message...")

# Process User Input
if user_input:
    st.session_state["messages"].append(("🧑‍💻 You:", user_input))
    responses = fetch_response(user_input)
    for bot_message in responses:
        st.session_state["messages"].append(("🤖 Chatbot:", bot_message))
        time.sleep(0.5)  # Simulate chatbot typing delay

# Display Chat History with Unique Keys
for index, (sender, text) in enumerate(st.session_state["messages"]):
    st.text_area(sender, value=text, height=100, key=f"chat_{index}")

# Frequently Asked Questions
st.write("## 📌 Popular Questions You Can Ask")
popular_questions = [
    "What is machine learning?",
    "How does deep learning work?",
    "What is natural language processing?",
    "How can I learn Python?",
    "What are ethical concerns in AI?",
    "What are the best resources for data science?",
    "How does AI impact education?",
    "What is supervised vs. unsupervised learning?"
]
for question in popular_questions:
    st.markdown(f"- {question}")

# Additional Features
st.write("## 💡 More Features Coming Soon!")
feature_list = [
    "Interactive Q&A based on your study topics.",
    "Personalized learning suggestions.",
    "AI-generated quizzes and exercises.",
    "Bookmark feature for saving responses.",
    "Voice-to-text input for convenience.",
    "Integration with Google Search for better answers.",
    "Real-time educational news updates.",
    "Student performance tracking and recommendations."
]
for feature in feature_list:
    st.markdown(f"- {feature}")

# Debugging & Admin Tools
st.sidebar.header("🐞 Debug Logs")
if "debug_logs" not in st.session_state:
    st.session_state["debug_logs"] = []
for log in st.session_state["debug_logs"]:
    st.sidebar.text(log)

st.sidebar.header("⚙️ Admin Tools")
if st.sidebar.button("Clear Chat History"):
    st.session_state["messages"] = []
    st.sidebar.success("Chat history cleared!")

# Display Chatbot Performance Statistics
st.write("## 📊 Chatbot Performance")
if "interaction_count" not in st.session_state:
    st.session_state["interaction_count"] = 0
st.session_state["interaction_count"] += 1
st.write(f"Total Interactions: {st.session_state['interaction_count']}")
