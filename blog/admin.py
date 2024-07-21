from django.contrib import admin
from .models import Post # 'models' module in the same directory as admin.py

# Register your models here.
admin.site.register(Post)
# Allows to create, update and delete blog posts from the admin panel.
# Each app has its own admin.py file