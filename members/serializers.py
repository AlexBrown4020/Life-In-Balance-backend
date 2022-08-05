from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Class
from classes.serializers import ClassSerializer

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)
    classes = serializers.ClassSerializer(Class, read_only=True, many=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2', 'classes', 'is_instructor']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()