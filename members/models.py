from django.db import models
from django.contrib.auth.models import User

class User(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()