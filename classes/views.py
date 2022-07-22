from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from .serializers import ClassSerializer
from .models import Class

class ClassGetAllView(generics.GenericAPIView):
    def get(request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return JsonResponse(serializer.data)