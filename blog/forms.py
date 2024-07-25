from .models import Comment
from django import forms

# Add a form for comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)  # imported from the Comment model
                            # the only data being sent through the form is the comment body