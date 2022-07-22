from rest_framework import serializers
from .models import Class

class ClassSerializer(serializers.ModeSerializer):
    class Meta:
        model = Class
        fields = ['id', 'title', 'description', 'date', 'time']