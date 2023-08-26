from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField("Date Created")
    ingredients = models.TextField()
    steps = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField("Date Last Updated")
    tags = models.CharField(max_length=1000)

