from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length = 100 , unique = True , verbose_name = "user_address" )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name = "article_author")
    title = models.CharField(max_length = 40 )
    content = models.TextField()
