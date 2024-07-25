from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.

# CLASS-BASED view that inherits from the generic.
# ListView class to display all posts.
# Requires as_view() in the urls.py
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # a collection of records from the database.
    template_name = "blog/index.html"
    paginate_by = 6

# The first argument sent to any Django view function is the request object
def post_detail(request, slug):
    """
    Function-based view:
    Displays an individual :model:`blog.Post`.

    **Template:**
    
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # return all comments related to the selected post
    # by using related_name="comments" (reverse lookup)
    comments = post.comments.all().order_by('-created_on')
    comment_count = post.comments.filter(approved=True).count()

    if request.method == 'POST':
        print('Received a POST request')
        comment_form = CommentForm(data=request.POST)
        print(comment_form)
        if comment_form.is_valid():  # checks our model to see the constraints on our fields i.e. we don't try to write
                                     # a null value to the database

            comment = comment_form.save(commit=False)  # returns an object that hasn't yet been saved to the database
                                                       # so that we can modify it further. We do this because we need 
                                                       # to populate the post and author fields before we save. 
                                                       # The object will not be written to the database until we call 
                                                       # the save method again.
            
            # Add the rest of the data required by the Comment model
            comment.author = request.user 
            comment.post = post

            # write the data to the database.
            comment.save  
            
            # When a message is added, it is displayed in the nav in base.html.
            messages.add_message(
                request, 
                messages.SUCCESS,  # message tag
                'Comment submitted and awaiting approval'
            )
            # You could use messages when a product is added or removed from a cart or when a form is submitted.
             

    # A blank instance of the CommentForm class. 
    # This line resets the content of the form to blank
    # so that a user can write a second comment if they wish.
    comment_form = CommentForm()  

    print('About to render template')



    return render(
        request,
        "blog/post_detail.html",
        {
            'post': post,
            "comments": comments,
            "comments_count": comment_count,
            "comment_form": comment_form,
        },  # {'post': post} dictionary is called context
                         # The context passes data from view to template
                         # The key name would be the same as the variable name passing through, 
                         # e.g. {"post": post}.
        
    )


