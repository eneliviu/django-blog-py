from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def my_blog(request):
    return HttpRequest('Hello, Blog!')
