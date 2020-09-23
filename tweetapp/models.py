from django.db import models

# Create your models here.

class PicTweetModel(models.Model):
    title = models.CharField(max_length=100)
    coment = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to='')
    author = models.CharField(max_length=100, null=True, blank=True)