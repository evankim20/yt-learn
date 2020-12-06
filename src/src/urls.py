"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# path(url, views function, url pattern name (for URL reversing)

from users.views import registration_view, login_view, logout_view
from common.views import landing_view, feed_view, entry_view, watch_view, search_view

# import template view from templates

urlpatterns = [
    path('', landing_view, name='landing'),
    path('feed', feed_view, name='feed'),
    path('entry', entry_view, name='entry'),
    path('admin/', admin.site.urls),
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    # path('insert', insert_view, name='insert'),
    path('watch', watch_view, name='watch'),
    path('search', search_view, name='search')
]
