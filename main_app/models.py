from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  comment = models.TextField(max_length=250)
  brand = models.CharField(max_length=50)
  price = models.IntegerField()
  url = models.URLField()
  image = models.CharField()

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="entry")
  name = models.CharField(max_length=50)
  comment = models.TextField(max_length=250)
  brand = models.CharField(max_length=50)
  price = models.IntegerField()
  url = models.URLField()
  image = models.CharField()