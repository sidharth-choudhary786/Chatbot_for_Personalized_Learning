import streamlit as st
import requests
from PIL import Image
import random
import time

# Streamlit Frontend for Rasa Chatbot
st.set_page_config(page_title="LearnAI", page_icon="🤖", layout="wide")

# Custom CSS for Vibrancy & Interactivity
st.markdown("""
<style>
/* Global Background */
body {
    background: linear-gradient(to right, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1, #fad0c4, #ff9a9e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Poppins', sans-serif;
    color: #333;
}

/* Sidebar Styling */
.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: #2d3436;
    margin-bottom: 15px;
    text-shadow: 1px 1px #dfe6e9;
}

.sidebar-section {
    background: linear-gradient(135deg, #74ebd5, #acb6e5);
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    color: white;
    font-weight: bold;
    transition: transform 0.3s, background 0.3s;
}

.sidebar-section:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
}

/* Chat Container */
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    padding: 15px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

/* Chat Bubbles */
.chat-message {
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 16px;
    font-weight: 500;
    animation: fadeIn 0.4s ease-in-out;
}

.chat-message.user {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    text-align: left;
    margin-left: auto;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

.chat-message.bot {
    background: linear-gradient(to right, #fad0c4, #fbc2eb);
    color: #333;
    text-align: left;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #ff9966, #ff5e62);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
    transition: transform 0.3s ease, background 0.3s ease-in-out;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.stButton>button:hover {
    background: linear-gradient(to right, #ff5e62, #ff9966);
    transform: scale(1.1);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
}

/* Floating Action Button */
.floating-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    text-align: center;
    font-size: 30px;
    line-height: 60px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    animation: bounce 2s infinite;
}

.floating-btn:hover {
    background: linear-gradient(to right, #2575fc, #6a11cb);
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

# Sidebar Branding
st.sidebar.image("Image.jpeg", caption="LearnAI", use_container_width=True)
st.sidebar.markdown('<h2 class="sidebar-title">AI/ML Chatbot</h2>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="sidebar-section">
📚 Learn interactively about AI, ML, DevOps, and more!
</div>
<div class="sidebar-section">
🚀 Key Features:
<ul>
  <li>Dynamic Learning Suggestions</li>
  <li>Interactive Visuals</li>
  <li>AI Fun Facts</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Floating Help Button
st.markdown('<div class="floating-btn">❓</div>', unsafe_allow_html=True)

# Main Page Header
st.title("Welcome to LearnAI! 🤖")
st.markdown("""
Your vibrant, interactive chatbot for AI/ML learning!  
Type your queries below and enjoy the experience. 🌈
""")

# Backend URL (Update with your Rasa server endpoint)
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
def display_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state["messages"]:
        if msg["sender"] == "user":
            st.markdown(f'<div class="chat-message user">YOU: {msg["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot">BOT: {msg["text"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# User input field
st.markdown("### Ask me anything about AI/ML:")
user_input = st.text_input("", "", placeholder="Type your message here...")

# Send user input to the bot
if st.button("Send") and user_input:
    st.session_state["messages"].append({"sender": "user", "text": user_input})
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_input})
        response_data = response.json()
        for bot_message in response_data:
            st.session_state["messages"].append({"sender": "bot", "text": bot_message["text"]})
    except Exception as e:
        st.error(f"Error communicating with the bot: {e}")

# Display updated chat
display_chat()


# Sidebar dropdown menu for topic selection
topic = st.sidebar.selectbox(
    "Select a topic to get book recommendations:",
    ["Select a topic", "AI", "Machine Learning", "Deep Learning", "Data Science", "NLP"]
)

# Dictionary with book recommendations for each topic
book_recommendations = {
    "AI": [
        "1. Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig",
        "2. Superintelligence: Paths, Dangers, Strategies by Nick Bostrom",
        "3. The Age of Em: Work, Love, and Life when Robots Rule the Earth by Robin Hanson"
    ],
    "Machine Learning": [
        "1. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron",
        "2. Pattern Recognition and Machine Learning by Christopher Bishop",
        "3. Machine Learning Yearning by Andrew Ng"
    ],
    "Deep Learning": [
        "1. Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville",
        "2. Neural Networks and Deep Learning by Michael Nielsen",
        "3. Deep Reinforcement Learning Hands-On by Maxim Lapan"
    ],
    "Data Science": [
        "1. Data Science for Business by Foster Provost and Tom Fawcett",
        "2. Python Data Science Handbook by Jake VanderPlas",
        "3. Practical Data Science with R by Nina Zumel and John Mount"
    ],
    "NLP": [
        "1. Speech and Language Processing by Daniel Jurafsky and James H. Martin",
        "2. Natural Language Processing with Python by Steven Bird, Ewan Klein, and Edward Loper",
        "3. Transformers for Natural Language Processing by Denis Rothman"
    ]
}

# Display book recommendations based on the selected topic in the sidebar
if topic != "Select a topic":
    st.sidebar.write(f"### Book Recommendations for {topic}:")
    for book in book_recommendations.get(topic, []):
        st.sidebar.write(book)

import csv

# Create a container for the feedback buttons at the bottom-right corner
st.markdown("""
    <style>
    .feedback-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        z-index: 100;
    }
    .feedback-button {
        background-color: #ff9a9e;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        cursor: pointer;
        font-weight: bold;
        font-size: 18px;
        color: white;
        transition: background-color 0.3s;
    }
    .feedback-button:hover {
        background-color: #ff5e62;
    }
    </style>
""", unsafe_allow_html=True)


# Function to save feedback to a CSV file
def save_feedback(feedback):
    # Open the CSV file in append mode to add new feedback
    with open("feedback.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write only the feedback (no timestamp)
        writer.writerow([feedback])


# Display feedback buttons
with st.container():
    st.markdown('<div class="feedback-container">', unsafe_allow_html=True)

    # Positive feedback button (Thumbs Up)
    if st.button("👍", key="positive_feedback", help="Thumbs Up - Positive Feedback"):
        save_feedback("positive")  # Save only "positive" to CSV
        st.write("Thank you for your positive feedback!")

    # Negative feedback button (Thumbs Down)
    if st.button("👎", key="negative_feedback", help="Thumbs Down - Negative Feedback"):
        save_feedback("negative")  # Save only "negative" to CSV
        st.write("Sorry to hear that! We appreciate your feedback.")

    st.markdown('</div>', unsafe_allow_html=True)
