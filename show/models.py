from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


def upload_show_cat(self, filename):
    url = 'data/show/cat'
    return url

def upload_show_subcat(self, filename):
    url = 'data/show/subcat'
    return url

def upload_show(self, filename):
    url = 'data/show/shows'
    return url


# Create your models here.
class ShowCategory(models.Model):
    title = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_show_cat, blank=True)
    def __str__(self):
        return f"{self.title}"

class ShowSubCategory(models.Model):
    cat = models.ForeignKey(ShowCategory, on_delete=models.CASCADE, related_name="shows_cat")
    title = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_show_subcat, blank=True)
    def __str__(self):
        return f"{self.title}"

class Shows(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.FileField(upload_to=upload_show, blank=True)
    banner = models.FileField(upload_to=upload_show, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    video = models.FileField(upload_to=upload_show, blank=True)
    category = models.ForeignKey(ShowCategory,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(ShowSubCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"