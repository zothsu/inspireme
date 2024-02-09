from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=50)
  comment = models.TextField(max_length=250)
  brand = models.CharField(max_length=50)
  price = models.IntegerField()
  product_url = models.URLField()
  image_url = models.CharField()

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='entry')
  product_name = models.CharField(max_length=50)
  body = models.TextField(max_length=250)
  brand = models.CharField(max_length=50)
  price = models.IntegerField()
  product_url = models.URLField()
  image_url = models.CharField()
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.post.title, self.name)