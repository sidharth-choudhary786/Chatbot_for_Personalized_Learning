# Chatbot_for_Personalized_Learning
Chatbot for Personalized Learning (Rasa) in AI and ML

# Description:
This Rasa Open Source-powered AI chatbot is designed to support learners in AI and ML by understanding intents and delivering accurate, context-aware responses. It simplifies complex concepts, answers questions, and provides resources for a seamless learning experience. Explore more on the GitHub repository!
# Features 
AI-Powered Intelligence

Custom Training: Utilizes ML to understand user intent and extract key entities.
Focused Expertise: Specially designed for AI and ML education.
Smart Responses: Handles multi-layered queries with precision.
Seamless Integration: Compatible with Telegram, Slack, and custom platforms.

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
nlu.yml, stories.yml, and domain.yml files are needed to Modify.
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
Introduce advanced features for seamless functionality.
Optimize training data for superior intent detection and entity recognition.
Extend API integrations for enhanced capabilities.

# Contributors
Lead Developer: Sidharth Choudhary
