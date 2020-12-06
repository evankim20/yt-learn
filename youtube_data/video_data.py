from googleapiclient.discovery import build
from sentiment_analysis import sentiment_score
from text_preprocessing import preprocess_text
import preprocessor as p
import configparser
from pprint import pprint
import configparser
import pandas as pd
import json
import os

#constants
API_SERVICE = 'youtube'
API_VERSION = 'v3'
MAX_COMMENTS = 400
CONFIG_FILE = 'creds.ini' 

#read api key from creds.ini
directory_path = os.path.abspath(os.path.dirname(__file__))
config_file_path = os.path.join(directory_path, CONFIG_FILE)

config = configparser.ConfigParser()
config.read(config_file_path)
API_KEY = config['youtube']['API_KEY']


def add_comments(result_items, comments):
    """ helper function to add comment text to our comment list """

    for item in result_items:
        comment = item['snippet']['topLevelComment']
        text = comment['snippet']['textOriginal']
        if(comment not in comments):
            comments.append(text)

def get_comments(youtube, video_id):
    """ get up to MAX_COMMENTS comments of a youtube video """

    comments = []
    total_comments = 0
    pulled_comments = 100

    request = youtube.commentThreads().list(
            part = "snippet,replies", 
            videoId = video_id, 
            maxResults = pulled_comments
            )
    results = request.execute()

    total_comments+=pulled_comments
    add_comments(results['items'], comments)

    while("nextPageToken" in results and total_comments<MAX_COMMENTS):
        request = youtube.commentThreads().list(
            part = "snippet,replies", 
            videoId = video_id, 
            pageToken= results["nextPageToken"],
            maxResults = pulled_comments
        )
        results = request.execute()
        total_comments+=pulled_comments

        add_comments(results['items'], comments)

    return comments

def get_statistics(youtube, video_id):
    """ retrieve like to dislike ratio """

    request = youtube.videos().list(
        part = "statistics",
        id = video_id
    )
    results = request.execute()

    statistics = results['items'][0]['statistics']

    like_count = int(statistics['likeCount'])
    dislike_count = int(statistics['dislikeCount'])
    total_views = int(statistics['viewCount'])

    return (like_count, dislike_count, total_views)


def get_video_id(url):
    """ get the video id from a given url (video id are 11 char)""" 

    id_index = url.index("v") + 2
    return url[id_index : id_index + 11]

if __name__ == "__main__":
    youtube = build('youtube','v3', developerKey=API_KEY)
    
    video_url = "https://www.youtube.com/watch?v=HPJKxAhLw5I"
    video_id = get_video_id(video_url)


    comments = get_comments(youtube, video_id)

    comments_df = pd.DataFrame(comments, columns = ['comments'])
    sentiment_score = sentiment_score(comments_df)
