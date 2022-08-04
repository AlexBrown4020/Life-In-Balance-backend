from django.db import models
from django.contrib.auth.models import User

class User(models.Model):

    username = models.CharField(max_length=30, required=True, unique=True)
    email = models.EmailField(required=True, unique=True)
    password = models.CharField(required=True)