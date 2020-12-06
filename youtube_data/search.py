from youtubesearchpython import SearchVideos
import json
from pprint import pprint 

def youtube_search(search_query, num_videos):
  """ return the top n posts based on query"""

  video_data = {

  }

  search = SearchVideos(search_query, offset=1, mode="json",
   max_results = num_videos).result()
  result = json.loads(search)
  videos = result['search_result']
  pprint(videos)
