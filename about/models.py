from django.db import models

# Create your models here.
class About(models.Model):
    
    title = models.CharField(max_length=200, default='About Me')

    updated_on = models.DateTimeField(auto_now=True)  # update datetime at each update 

    content = models.TextField()

    def __str__(self):
        return f"About me {self.title} updated on {self.updated_on}"


