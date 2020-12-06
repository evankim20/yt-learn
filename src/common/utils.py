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
