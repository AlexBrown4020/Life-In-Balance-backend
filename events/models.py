from django.db import models
from datetime import datetime
from members.models import *

class Event(models.Model):
    creator = models.ForeignKey('Member', on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, null=True)
    time = models.DateTimeField(default=datetime.now, null=True)
    description = models.TextField(max_length=255, null=True)
    participants = models.ManyToManyField('Member', related_name='participants', blank=True)

    def __str__(self):
        return self.title