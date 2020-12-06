from youtubesearchpython import SearchVideos
from common.utils import SearchResult
import json
from pprint import pprint 

# def youtube_search(search_query, num_videos):
#   """ return the top n posts based on query"""

#   video_data = []

#   search = SearchVideos(search_query, offset=1, mode="json",
#    max_results = num_videos).result()
#   result = json.loads(search)
#   videos = result['search_result']


#   for video in videos:
#     thumbnail = [thumbnail for thumbnail in video['thumbnails'] if thumbnail.endswith('sddefault.jpg')][0]
#     video_id = video['id']
#     title = video['title']
#     view_count = video['views']
    
#     print(video)

#     search_result = SearchResult(video['id'], video['title'], video['views'], video['channel'], video['thumbnails'][0])


def get_video_data(search_query, num_videos):
  """ gets top num_videos from youtube search """

  search = SearchVideos(search_query, offset=1, mode="json",
   max_results = num_videos).result()
  result = json.loads(search)
  videos = result['search_result']

  search_results = []

  for video in videos:
    thumbnail = [thumbnail for thumbnail in video['thumbnails'] if thumbnail.endswith('sddefault.jpg')][0]
    search_results.append(SearchResult(video['id'], thumbnail, video['title'],video['channel']))

  return search_results
  



