from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


def upload_movie_cat(self, filename):
    url = 'data/movie/cat'
    return url

def upload_movie_subcat(self, filename):
    url = 'data/movie/subcat'
    return url

def upload_movie_genre(self, filename):
    url = 'data/movie/genre'
    return url

def upload_movie_producer(self, filename):
    url = 'data/movie/producer'
    return url

def upload_movie_reels(self, filename):
    url = 'data/movie/reels'
    return url

def upload_movie(self, filename):
    url = 'data/movie/movie'
    return url



class MovieCategory(models.Model):
    title = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie_cat, blank=True)
    def __str__(self):
        return f"{self.title}"

class MovieGenre(models.Model):
    title = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie_genre, blank=True)
    def __str__(self):
        return f"{self.title}"
    
class MovieSubcategory(models.Model):
    title = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie_subcat, blank=True)
    category = models.ForeignKey(MovieCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"
    
class MovieProducer(models.Model):
    name = models.TextField(blank=True)
    company = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie_producer, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    phone = models.TextField(blank=True)
    reports = models.JSONField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

class MovieReels(models.Model):
    name = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie_reels, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    video = models.FileField(upload_to=upload_movie_reels, blank=True)
    def __str__(self):
        return f"{self.name}"

class Movies(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_movie, blank=True)
    banner = models.FileField(upload_to=upload_movie, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    video = models.FileField(upload_to=upload_movie, blank=True)
    category = models.ForeignKey(MovieCategory,on_delete=models.CASCADE,related_name="movieCat")
    sub_category = models.ForeignKey(MovieSubcategory,on_delete=models.CASCADE)
    genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE, null=True, blank=True)
    Price = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return f"{self.title}"