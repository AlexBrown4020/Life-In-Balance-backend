from django.db import models
from django.contrib.auth.models import User
from classes.models import Class

class User(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    is_instructor = models.BooleanField(default=False)