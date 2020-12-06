from django.db import models

# Create your models here.


class Video(models.Model):

    video_id = models.CharField(max_length=15)
    title = models.CharField(max_length=70)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    channel = models.CharField(max_length=40) #we want this to point to a channel
    thumbnail = models.CharField(max_length=70)
    sentiment_score = models.FloatField()

    def __init__(self, video_id, title, view_count, like_count, dislike_count, channel, thumbnail, sentiment_score):
        super().__init__(video_id, title, view_count, like_count, dislike_count, channel, thumbnail, sentiment_score)
        self.video_id = video_id
        self.title = title
        self.view_count = view_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.channel = channel #we want this to point to a channel
        self.thumbnail = thumbnail
        self.sentiment_score = sentiment_score


    # # what django shows on backend
    # BEGINNER = 'Beginner'
    # ADVANCED = 'Advanced'

    # # what django shows on frontend
    # SKILL_CHOICES = (
    #     (BEGINNER,'Beginner'),
    #     (ADVANCED,'Advanced'),
    # )


    # # data from our users
    # skill_level = models.CharField(max_length=15, choices=SKILL_CHOICES, default=BEGINNER)



