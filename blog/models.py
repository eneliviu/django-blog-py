from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# A draft is defined as 0 and published as 1 
# The default is to save as a draft (STATUS == 0).

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    # The title values should be unique to avoid having blog posts
    #  of the same name confusing your users.
    
    slug = models.SlugField(max_length=200, unique=True)
    # the slug is what is used to build a URL for each post
    
    author = models.ForeignKey(
                               User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts'
                            )
    # One user can write many posts, so this is a one-to-many or Foreign Key. 
    # The cascade on delete means that on the deletion of the user entry,
    # all their posts are also deleted.

    content = models.TextField()
    # This is the blog article content.

    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True means the default created time is the time of post entry

    status = models.IntegerField(choices=STATUS, default=0)
    # this uses a constant STATUS

    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Title: {self.title} | written by {self.author}"


    # The Meta class provides additional information or metadata about the model.
    class Meta:
        ordering = ["-created_on"]



class Comment(models.Model):
    
    
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commenter'
    )

    body = models.TextField()

    approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    class Meta:
        ordering = ["created_on"]
