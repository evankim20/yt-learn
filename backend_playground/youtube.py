from googleapiclient.discovery import build
import json
from pprint import pprint

API_SERVICE = 'youtube'
API_VERSION = 'v3'
api_key  = 'AIzaSyC48wMVDzc_mz5zJHbhhC901qiYcQ4iaMs'


def get_comments(youtube,parent_id):
    comments = []

    request = youtube.commentThreads().list(
            part="snippet,replies", 
            videoId= parent_id
            )
    results = request.execute()

    num_comments = len(results) -1

    for i in range(0, num_comments):
        comments = results['kind']
        text 

    
    pprint(results)


def parse_url(url):
    """ get the video id from a given url """ 
    delimeter = "v="
    return url.split(delimeter)[1]
  

if __name__ == "__main__":
    youtube = build('youtube','v3', developerKey= api_key)
    
    video_url = "https://www.youtube.com/watch?v=m0RWSHdS77E"
    video_id = parse_url(video_url)

    get_comments(youtube,video_id)