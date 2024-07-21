from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
# Allows to create, update and delete blog posts from the admin panel.