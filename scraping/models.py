from django.db import models
from django.contrib.auth.models import AbstractUser


class Scraping(models.Model):
    scraping_id = models.AutoField(primary_key=True)
    scraping_heading = models.CharField(max_length=250)
    scraping_body = models.TextField()

class Article(models.Model):
    article = models.URLField()
    title = models.CharField(max_length=250)

class History(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class User(AbstractUser):
    username = models.CharField(('username'), max_length=150, unique=True)
    email = models.EmailField(('email address'), unique=True)