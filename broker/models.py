from django.db import models
from django.contrib.auth.models import User
from photos.models import Category
from django.utils import timezone
# Create your models here.


#Broker File details
class Broker(models.Model):
    class Meta:
        verbose_name = 'Broker'
        verbose_name_plural = 'Broker'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    playstore_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    pinterest_url = models.CharField(max_length=200, null=True, blank=True)
    youtube_url = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description
