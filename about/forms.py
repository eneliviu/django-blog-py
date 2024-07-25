from .models import CollaborateRequest
from django import forms

# Add a form for Collaboration requests

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')