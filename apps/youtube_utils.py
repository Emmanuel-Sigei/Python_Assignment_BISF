# Import the necessary libraries
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load your YouTube API key from the .env file
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube_videos(query, max_results=10):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    try:
        # Execute a search request
        search_response = youtube.search().list(
            q=query,
            type="video",
            maxResults=max_results,
            part="snippet"  # You should add the "part" parameter
        ).execute()

        # Log the API response for debugging
        print("YouTube API Response:", search_response)

        videos = []
        for search_result in search_response.get("items", []):
            video = {
                "title": search_result["snippet"]["title"],
                "video_id": search_result["id"]["videoId"]
            }
            videos.append(video)

        return videos

    except Exception as e:
        print("Error fetching YouTube videos:", str(e))
        return []


# You can call this function to get a list of video dictionaries
