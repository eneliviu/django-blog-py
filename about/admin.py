from django.contrib import admin
from .models import About # 'models' module in the same directory as admin.py
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# Each app has its own admin.py file

# Allows to create, update and delete blog posts from the admin panel.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    # list_display = ('title', 'updated_on')
    # search_field = ['title', 'content']
    # list_filter = ('updated_on',)
    # prepopulated_fields = {'title': ('title',)}
    summernote_fields = ('content',)


