from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
import logging
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

class ActionGenerateContent(Action):
    def __init__(self):
        self.model_name = "google/flan-t5-large"
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            logger.info(f"Successfully loaded the model: {self.model_name}.")
        except Exception as error:
            logger.error(f"Failed to load the model: {error}")
            self.model = None
            self.tokenizer = None

    def name(self) -> Text:
        return "action_generate_content"

    def generate_prompt(self, topic: str) -> str:
        return (
            f"Provide an in-depth and accessible explanation about {topic}.\n"
            f"Details to include:\n"
            f"- Overview and core ideas\n"
            f"- Key principles or elements\n"
            f"- Real-world uses or case studies\n"
            f"- Significant facts and developments\n"
            f"- Emerging trends or potential future directions\n"
            f"Ensure clarity and comprehensiveness in the explanation."
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        if not self.model or not self.tokenizer:
            dispatcher.utter_message(text="I'm currently unable to process your request. Please try again later.")
            return []

        topic = next(tracker.get_latest_entity_values("topic"), None)
        if not topic:
            dispatcher.utter_message(text="Could you specify the topic you'd like to know about?")
            return []

        restricted_keywords = [
            "pizza", "food", "Infosys", "company", "movie", "celebrity", "sports",
            "music", "recipe", "travel", "fashion", "gossip", "weather",
            "news", "politics", "games", "shopping", "cars"
        ]
        if any(keyword in topic.lower() for keyword in restricted_keywords):
            dispatcher.utter_message(text="That topic doesn't seem educational. Please ask about another topic.")
            return []

        try:
            input_text = self.generate_prompt(topic)
            inputs = self.tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)

            outputs = self.model.generate(
                inputs.input_ids,
                max_length=512,
                min_length=100,
                num_beams=5,
                temperature=0.7,
                top_p=0.92,
                top_k=50,
                repetition_penalty=2.5,
                length_penalty=1.5,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

            content = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            formatted_content = content.replace(". ", ".\n\n")

            dispatcher.utter_message(text=f"Here is a detailed explanation on {topic}:\n\n{formatted_content}")
            logger.info(f"Generated content for topic: {topic}")

        except Exception as error:
            logger.error(f"Content generation failed: {error}")
            dispatcher.utter_message(text="I encountered an issue generating the content. Please try again later.")

        return [SlotSet("topic", topic)]


class ActionFetchYouTubeVideos(Action):
    def __init__(self):
        try:
            self.youtube = build("youtube", "v3", developerKey="AIzaSyAt-V4r_RNv-IWfOADeCbkkwBqZSD54hSg")
            logger.info("YouTube API client initialized successfully.")
        except Exception as error:
            logger.error(f"Failed to initialize YouTube API client: {error}")
            self.youtube = None

    def name(self) -> Text:
        return "action_fetch_youtube_videos"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        if not self.youtube:
            dispatcher.utter_message(text="I can't access YouTube at the moment. Please try again later.")
            return []

        query = tracker.get_slot("youtube_query")
        if not query:
            dispatcher.utter_message(text="Could you tell me what you're searching for on YouTube?")
            return []

        try:
            search_response = self.youtube.search().list(
                q=query,
                part="snippet",
                type="video",
                maxResults=3
            ).execute()

            videos = search_response.get("items", [])
            if not videos:
                dispatcher.utter_message(text=f"No results found for '{query}'.")
                return []

            response_message = "Here are some YouTube videos you might find helpful:\n"
            for video in videos:
                title = video["snippet"]["title"]
                video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                response_message += f"- {title}: {video_url}\n"

            dispatcher.utter_message(text=response_message)

        except Exception as error:
            logger.error(f"Error fetching videos: {error}")
            dispatcher.utter_message(text="Something went wrong while fetching videos. Please try again.")

        return []
