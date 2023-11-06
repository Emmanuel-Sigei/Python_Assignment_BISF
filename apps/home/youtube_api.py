import json
import os
import requests

# Get your YouTube API key from the environment variable
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_videos(query):
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': query,
        'maxResults': 10,
        'key': YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = json.loads(response.content)

    videos = []
    for item in data['items']:
        video = {
            'title': item['snippet']['title'],
            'thumbnail_url': item['snippet']['thumbnails']['high']['url'],
            'video_url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
        }
        videos.append(video)

    return videos
