import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load your YouTube API key from the .env file
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Print the loaded YouTube API Key
print("Loaded YouTube API Key:", YOUTUBE_API_KEY)

def search_youtube_videos(query, max_results=10):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    try:
        search_response = youtube.search().list(
            q=query,
            type="video",
            maxResults=max_results
        ).execute()

        videos = []

        for search_result in search_response.get("items", []):
            video = {
                "title": search_result["snippet"]["title"],
                "video_id": search_result["id"]["videoId"]
            }
            videos.append(video)

        # Debug: Print the retrieved videos
        print("Retrieved Videos:", videos)

        return videos

    except Exception as e:
        print("Error fetching YouTube videos:", str(e))
        return []

