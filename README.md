# Chatbot_for _personalized_learning
Rasa Chatbot for Personalized Learning in AI and ML

# Description:
This project is a conversational AI chatbot built using Rasa Open Source, designed to support learners in the fields of Artificial Intelligence and Machine Learning. By understanding user intents and providing relevant responses, the chatbot serves as a helpful guide for learners by answering questions, offering detailed explanations, and navigating various AI/ML concepts. For more information, visit the GitHub repository.

# Features
Custom-Trained Model: Leverages machine learning to interpret user intents and extract relevant entities.

Domain-Specific Expertise: Tailored specifically for the AI and machine learning educational domain.

Multi-Intent Handling: Processes and responds to complex, multi-layered queries effectively.

Integration-Ready: Easily integrates with platforms like Telegram, Slack, or custom websites.

# Installation
   # Prerequisites:

     -Python 3.8 or later
     -Rasa Open Source
     -Virtual environment (recommended)

# Steps:

  Clone the Repository:
     git clone(https://github.com/AdJuSingh/Ed_bot.git) 
     
  Navigate to the Project Directory:

     cd PythonProject2  
     
  Create and Activate a Virtual Environment:
  
     1.python -m venv .venv  
     2..venv\Scripts\activate  
     
  Install Dependencies:
  
     pip install -r requirements.txt  
     
# Training the Model
Modify the nlu.yml, stories.yml, and domain.yml files as needed.
Train the model using cmd:
     rasa train  
The trained model will be saved in the models/ directory.

Running the Chatbot
On the Command Line:

Run the chatbot interactively:
     rasa shell  
   
As a Server:

Run the chatbot as a server:
     rasa run  
   
# Files and Directories
data: Contains training data for intents and stories.

domain.yml: Defines intents, entities, actions, and responses.

models: Stores trained models.

actions: Holds custom action scripts.

config.yml: Specifies the pipeline and policies used for the chatbot.

# Future Enhancements
Add support for new features and functionalities.
Enhance training data for improved intent classification and entity recognition.
Expand integration with external APIs for advanced interactions.

# Contributors
Lead Developer: Aditi Jai Singh
