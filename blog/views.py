from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

# Class-based view that inherits from the generic.ListView class to display all posts.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # a collection of records from the database.
    template_name = "blog/index.html"
    paginate_by = 6
