from django.db import models

# Create your models here.


class Video(models.Model):
    video_id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=70, unique=True)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()

    # we want this to point to a channel
    channel = models.CharField(max_length=40)
    thumbnail = models.CharField(max_length=70)
    sentiment_score = models.FloatField()

    def __str__(self):
        return self.title


class Channel(models.Model):
    channel_id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

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
