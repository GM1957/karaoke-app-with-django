from django.db import models

# Create your models here.
class Song(models.Model):
    sno = models.AutoField(primary_key=True)
    songFile = models.FileField(upload_to="home/music",blank=True)
    songName = models.CharField(max_length=500)
    image = models.ImageField(upload_to="home/images/songimages",blank=True)
    slug = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.songName

class tempSong(models.Model):
    TSsno = models.AutoField(primary_key=True)
    tempSongFile = models.FileField(upload_to="home/music/tempFile")
    
