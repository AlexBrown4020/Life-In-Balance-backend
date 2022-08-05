from django.db import models
from events.models import Event

class Member(models.Model):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    classes = models.ManyToManyField(Event, related_name='classes', blank=True)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.username