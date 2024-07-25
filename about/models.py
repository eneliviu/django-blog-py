from django.db import models

# Create your models here.
# Run: 
# python3 manage.py makemigrations
# python3 manage.py migrate  
# each time a model is declared or modeified


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"Collaboration request from {self.name}"




