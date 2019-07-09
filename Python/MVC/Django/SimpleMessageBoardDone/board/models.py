from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length = 500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
class Post(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)
    def __str__(self):
        return self.topic.title

# category model

# future add comments model