import json
from youtubesearchpython import SearchVideos

class SearchResult:
    def __init__(self, id, title, views, channel):
        self.id = id
        self.title = title
        self.views = views
        self.channel = channel

    def __str__(self):
        return self.id + ' | ' + self.title + ' | ' + str(self.views) + ' | ' + self.channel

def search_yt(term):

    output = []

    # grab search results
    search = SearchVideos(term, offset=1, mode="json", max_results=5)
    raw = search.result()
    raw = json.loads(raw)
    raw = raw['search_result']


    for x in raw:
        temp = SearchResult(x['id'], x['title'], x['views'], x['channel'])
        output.append(temp)

    return output


