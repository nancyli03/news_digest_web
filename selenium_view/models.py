from django.db import models

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
