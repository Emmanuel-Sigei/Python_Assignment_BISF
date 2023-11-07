# -*- encoding: utf-8 -*-
"""
Python_Assignment
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# Import the function to retrieve YouTube videos
from apps.youtube_utils import search_youtube_videos

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

        print("YouTube API Response:", search_response)  # Add this line to log the API response
        return videos

    except Exception as e:
        print("Error fetching YouTube videos:", str(e))
        return []


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment
    except:
        return None
