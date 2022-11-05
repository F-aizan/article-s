from django.db import models

# Create your models here.

class Articles(models.Model):
    id = models.IntegerField(primary_key=True)
    articles = models.CharField(max_length=400)