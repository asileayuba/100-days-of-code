from django.db import models

# Create your models here.

class TotalViewsModel(models.Model):
    label = models.CharField(max_length=50)
    views =models.IntegerField()
    
    
class MostWatchedVideos(models.Model):
    title = models.CharField(max_length=50)
    views_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)