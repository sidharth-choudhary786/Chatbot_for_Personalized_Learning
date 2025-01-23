from googleapiclient.discovery import build
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionFetchYouTubeVideos(Action):
    def name(self):
        return "action_fetch_youtube_videos"

    def run(self, dispatcher, tracker, domain):
        # Get the user's query from the conversation
        query = tracker.get_slot("youtube_query")  # Assuming "youtube_query" is a slot

        if not query:
            dispatcher.utter_message("Please specify what you're looking for on YouTube.")
            return []

        try:
            # YouTube API setup
            api_key = "AIzaSyAt-V4r_RNv-IWfOADeCbkkwBqZSD54hSg"
            youtube = build("youtube", "v3", developerKey=api_key)

            # Search for videos matching the query
            search_response = youtube.search().list(
                q=query,
                part="snippet",
                type="video",
                maxResults=3
            ).execute()

            # Format the results
            videos = search_response.get("items", [])
            if not videos:
                dispatcher.utter_message(f"No videos found for '{query}'.")
                return []

            response_message = "Here are some YouTube videos I found:\n"
            for video in videos:
                title = video["snippet"]["title"]
                video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                response_message += f"- {title}: {video_url}\n"

            dispatcher.utter_message(response_message)
        except Exception as e:
            dispatcher.utter_message(f"An error occurred while fetching videos: {str(e)}")
            return []

        return []
