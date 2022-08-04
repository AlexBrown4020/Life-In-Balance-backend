from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'image']