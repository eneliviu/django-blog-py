from . import views
from django.urls import path

# This file is where we'll list our blog app-specific URLs.

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # class-based view, requires as_view()
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # url points to post_detail function-based view
    # '<slug:slug>/' is where the slug value is passed from the template's URL tag. 
    # This urlpattern creates a url path of the domain path plus the slug value.
    # The slug is used for the blog post path as it uniquely identifies the post and 
    # contains only characters valid for a URL.
    # slug before colon -> data type
    # slug after colon -> the post.slug value passed from the template (seen in the  browser bar)
    
    path('<slug:slug>/edit_comment/<int:comment_id>',
    views.comment_edit,
    name='comment_edit'),

    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete,
    name='comment_delete'),
    
]