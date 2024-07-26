from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
    Function-based view that displays an individual :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`
    ``comments``
        All approved comments related to the post
    ``comment_count``
        A count of approved comments related to the post
    ``comment_form``
        An isntance of :form:`blog.CommentForm`

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
        comment_form = CommentForm(data=request.POST)
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
            comment.save()  
            
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



def comment_edit(request, slug, comment_id):
    """ 
    View to edit comments
    """

    if request.method == 'POST':

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment,
                                    pk=comment_id) 
        comment_form = CommentForm(data=request.POST, 
                        instance=comment)  # Changes made to the form will be applied to the existing Comment,
                                           # instead of creating a new one.

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()

            messages.add_message(
                request, 
                messages.SUCCESS,
                'Comment updated!'
            )

        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))    


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Comment deleted'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
