from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

# Class-based view that inherits from the generic.ListView class to display all posts.
class PostList(generic.ListView):
    queryset = Post.objects.all()  # a collection of records from the database.
    #queryset = Post.objects.all().order_by('created_on')
    template_name = "post_list.html"
