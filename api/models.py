from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

def live_video(self, filename):
    url = 'data/live'
    return url

def video_advert(self, filename):
    url = 'data/videoAdvert'
    return url

def banner_advert(self, filename):
    url = 'data/bannerAdvert'
    return url

    
class LiveTv(models.Model):
    name = models.TextField(blank=True)
    link = models.TextField(blank=True)
    image = models.FileField(max_length=255, upload_to=live_video,)
    
class VideoAdvert(models.Model):
    name = models.CharField(max_length=255, null=True)
    desc = models.TextField(blank=True)
    skip = models.BooleanField(default=False)
    image = models.FileField(max_length=255, upload_to=video_advert)
    video = models.FileField(max_length=255, upload_to=video_advert)
    
class BannerAdvert(models.Model):
    name = models.TextField(blank=True)
    owner = models.TextField(blank=True)
    target = models.PositiveIntegerField()
    image = models.FileField(max_length=255, upload_to=banner_advert)

class GTerms(models.Model):
    content = models.TextField()
    
class PTerms(models.Model):
    content = models.TextField()