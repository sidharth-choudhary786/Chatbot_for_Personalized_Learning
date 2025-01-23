import streamlit as st

st.title("Chatbot on education")


st.write("Ask questions about AI, ML, DL, science, mathematics, history, or any subject you'd like to learn more about.")

def get_response(my_input):
    my_input = my_input.lower()

    if "math" in my_input:
        return "Mathematics is the study of numbers, shapes, and patterns. Do you need help with algebra, geometry, or calculus?"
    elif "science" in my_input:
        return "Science helps us understand the natural world. Are you interested in physics, chemistry, or biology?"
    elif "history" in my_input:
        return "History is the study of past events. Would you like to learn about ancient civilizations or modern history?"
    elif "programming" in my_input:
        return "Programming involves writing code to create software applications. Are you learning Python, Java, or another language?"
    elif "machine learning" in my_input or "ml" in my_input:
        return "Machine Learning is a subset of AI that allows systems to learn and improve from experience. Do you need help with supervised or unsupervised learning?"
    elif "deep learning" in my_input or "dl" in my_input:
        return "Deep Learning is a branch of Machine Learning that uses neural networks with many layers. Are you interested in neural networks, CNNs, or RNNs?"
    elif "artificial intelligence" in my_input or "ai" in my_input:
        return "Artificial Intelligence involves creating machines that can perform tasks requiring human-like intelligence. Are you interested in algorithms, natural language processing, or robotics?"
    else:
        return "I'm here to help with educational topics. Please ask me about a subject you're interested in!"

my_input = st.text_input("Ask me a question related to education:")

if my_input:
    response = get_response(my_input)
    st.write(f" Chatbot: {response}")
