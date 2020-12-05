from django.shortcuts import render

# Create your views here.

def landing_view(request):
    print('called landing')
    return render(request, 'landing.html')
