from . import views
from django.urls import path

# This file is where we'll list our blog app-specific URLs.

urlpatterns = [
    path('', views.about_me, name='about'),  # class-based view, requires as_view()
]