from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.CharField(max_length=1000)
    poster_path = models.CharField(max_length=1000)
    vote_average=models.CharField(max_length=20)
    vote_count=models.CharField(max_length=20)