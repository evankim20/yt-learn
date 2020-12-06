from django.db import models

# Create your models here.


class Video(models.Model):

    # youtube api stuff
    video_id = models.CharField(max_length=15)
    title = models.CharField(max_length=70)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    channel = models.CharField(max_length=40) #we want this to point to a channel
    thumbnail = models.CharField(max_length=70)
    sentiment_score = models.FloatField()

    # what django shows on backend
    BEGINNER = 'Beginner'
    ADVANCED = 'Advanced'

    # what django shows on frontend
    SKILL_CHOICES = (
        (BEGINNER,'Beginner'),
        (ADVANCED,'Advanced'),
    )

    '''
    POSITIVE =
    NEGATIVE = 
    NEUTRAL = 
    
    SENTIMENT_CHOICES = (
        (POSITIVE, ),
        (NEGATIVE, ),
        (NEUTRAL, ),
    )
    '''


    # data from our users
    skill_level = models.CharField(max_length=15, choices=SKILL_CHOICES, default=BEGINNER)

    # sentiment = models.CharField(max_length=15, choices=SENTIMENT_CHOICES, default=NEUTRAL)
    # rating =
    # overall_score =


