from . import views
from django.urls import path

# This file is where we'll list our blog app-specific URLs.

urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]