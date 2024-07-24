from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

# CLASS-BASED view that inherits from the generic.
# ListView class to display all posts.
# Requires as_view() in the urls.py
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # a collection of records from the database.
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Function-based view:
    Displays an individual :model:`blog.Post`.

    **Template:**
    
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)


    return render(
        request,
        "blog/post_detail.html",
        {'post': post},  # {'post': post} dictionary is called context
                         # The context passes data from view to template
                         # The key name would be the same as the variable name passing through, 
                         # e.g. {"post": post}.
    )


