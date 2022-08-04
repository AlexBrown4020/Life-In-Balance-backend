from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2']
