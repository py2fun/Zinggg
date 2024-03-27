from django.db import models

# Create your models here.

class Song(models.Model):
    track = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=70)
    lyrics = models.TextField(max_length=1000)
    length = models.TimeField()

class Playlist(models.Model):
    name= models.CharField(max_length=70)
    description= models.CharField(max_length=150)
    date_created= models.DateTimeField(auto_now_add=True)
    number_of_songs=models.IntegerField()
    



