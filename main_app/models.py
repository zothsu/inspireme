from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
  pass

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  comment = models.TextField(max_length=250)
  brand = models.CharField(max_length=50)
  price = models.IntegerField()
  url = models.URLField()
  image = models.CharField()

  

