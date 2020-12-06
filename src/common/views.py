from django.shortcuts import render

# Create your views here.

def landing_view(request):
    print('called landing')
    return render(request, 'landing.html')

def feed_view(request):
    temp_list = [{'video': 'video 1', 'teacher': 't1', 'stars': '5'}, {'video': 'video 2', 'teacher': 't2', 'stars': '4'},
                 {'video': 'video 3', 'teacher': 't3', 'stars': '3'}, {'video': 'video 3', 'teacher': 't3', 'stars': '3'},
                 {'video': 'video 3', 'teacher': 't3', 'stars': '3'}, {'video': 'video 3', 'teacher': 't3', 'stars': '3'},
                 {'video': 'video 3', 'teacher': 't3', 'stars': '3'}]
    context = {'entries': temp_list}
    return render(request, 'feed.html', context)

def entry_view(request):
    context = {'video': {'title': 'User Registration and Login Authentication | Django (3.0) Crash Course Tutorials (pt 14)', 'teacher': 'Dennis Ivy', 'stars': '5 stars'},
               'reviews': [{'name': 'Bob', 'stars': '4 stars', 'response': 'Great video!'}, {'name': 'Alice', 'stars': '1 stars', 'response': 'Video sucked'},
                           {'name': 'Karen', 'stars': '3 stars', 'response': 'meh'}]}
    return render(request, 'entry.html', context)