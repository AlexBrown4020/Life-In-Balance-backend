from django.db import models
from datetime import datetime

class Class(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, null=True)
    time = models.DateTimeField(default=datetime.now, null=True)
    description = models.TextField(max_length=255, null=True)