from django.shortcuts import render, redirect
from youtube_data.search import get_video_data
from youtube_data import sentiment_analysis
from youtube_data import video_data
from .models import Video
import pandas as pd
# import youtube_data.video_data
# import youtube_data.sentiment_analysis

# Create your views here.


def landing_view(request):
    print('called landing')
    return render(request, 'landing.html')


def feed_view(request):
    temp_list = [{'video': 'video 1', 'teacher': 't1', 'stars': 5}, {'video': 'video 2', 'teacher': 't2', 'stars': 4},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}, {
                     'video': 'video 3', 'teacher': 't3', 'stars': 3},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}, {
                     'video': 'video 3', 'teacher': 't3', 'stars': 3},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}]
    context = {'entries': temp_list}
    return render(request, 'feed.html', context)


def entry_view(request):
    context = {'video': {'title': 'User Registration and Login Authentication | Django (3.0) Crash Course Tutorials (pt 14)', 'teacher': 'Dennis Ivy', 'stars': 2.6},
               'reviews': [{'name': 'Bob', 'stars': 4, 'response': 'Great video!'}, {'name': 'Alice', 'stars': 1, 'response': 'Video sucked'},
                           {'name': 'Karen', 'stars': 3, 'response': 'meh'}]}
    return render(request, 'entry.html', context)


"""
insert_view handles the form POST request
"""


def insert_view(request):
    if request.POST:
        video_rating = request.POST.get('videorating')
        teacher_rating = request.POST.get('teacherrating')
        review = request.POST.get('review')

        # TODO: post to db and then redirect w/ updated info! (just grab from db again)
        print(f'Stuff: {video_rating}, {teacher_rating}, {review}')
        return redirect('entry')
    else:
        print("FAIL")
    return render(request, 'entry.html')


def search_view(request):
    if request.POST:
        search_query = request.POST.get('search_query')
        search_results = get_video_data(search_query, 2)

        for search_result in search_results:
            video_db_res = Video.objects.filter(video_id=search_result.id)
            if(not video_db_res):
                video_id = search_result.id
                comments = video_data.get_comments(
                    video_data.youtube, video_id)
                comments_df = pd.DataFrame(comments, columns=['comments'])
                sentiment = sentiment_analysis.sentiment_score(comments_df)
                like_count, dislike_count, total_views = video_data.get_statistics(
                    video_data.youtube, video_id)

                new_vid = Video(
                    video_id,
                    search_result.title,
                    total_views,
                    like_count,
                    dislike_count,
                    search_result.channel,
                    search_result.thumbnail,
                    sentiment
                )
                new_vid.save()

        # TODO: assign fake star ratings
        context = []
        context = {'entries': context}

        return render(request, 'feed.html', context)


def watch_view(request):
    context = {}

    video_id = 'UmljXZIypDc'

    context['vid_url'] = video_id
    return render(request, 'common/watch.html', context)
