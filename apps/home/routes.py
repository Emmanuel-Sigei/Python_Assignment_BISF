# Import the necessary modules
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from googleapiclient.discovery import build
import os
import json

# Initialize the YouTube Data API client with your API key
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_videos(query):
    """
    Get a list of YouTube videos for the given query.

    Args:
        query: The search query.

    Returns:
        A list of dictionaries, each containing the following information about a video:
            * title: The title of the video.
            * thumbnail_url: The URL of the video's thumbnail.
            * video_url: The URL of the video.
    """

    youtube_data_api = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    search_response = youtube_data_api.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=10
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append({'title': search_result['snippet']['title'], 'thumbnail_url': search_result['snippet']['thumbnails']['high']['url'], 'video_url': video_url})

    return videos

# Your existing code ...

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None

@blueprint.route('/youtube_videos')
@login_required
def youtube_videos():
    videos = get_videos('Gender Based Violence')
    return render_template('home/youtube_videos.html', youtube_videos=videos)
