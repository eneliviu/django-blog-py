from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

# Class-based view that inherits from the generic.ListView class to display all posts.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
