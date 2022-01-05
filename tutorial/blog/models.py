from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length=255, unique=True)
    # Slug = /nomesinho unico
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    