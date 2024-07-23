from django.contrib import admin
from .models import Post, Comment # 'models' module in the same directory as admin.py
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# Each app has its own admin.py file


# Allows to create, update and delete blog posts from the admin panel.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_field = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)