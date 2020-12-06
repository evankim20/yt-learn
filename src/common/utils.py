import json
from youtubesearchpython import SearchVideos

class SearchResult:
    def __init__(self, id, thumbnail, title,channel):
        self.id = id
        self.thumbnail = thumbnail
        self.title = title
        self.channel = channel

    def __str__(self):
        return self.id + ' | ' + self.title + ' | ' + str(self.views) + ' | ' + self.channel

