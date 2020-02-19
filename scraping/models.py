from django.db import models

class Scraping(models.Model):
    scraping_id = models.AutoField(primary_key=True)
    scraping_heading = models.CharField(max_length=250)
    scraping_body = models.TextField()