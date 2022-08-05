from django.db import models
from classes.models import Class

class Member(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    classes = models.ManyToManyField(Class, related_name='classes', blank=True)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.username