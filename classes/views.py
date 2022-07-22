from django.shortcuts import render
from django.http import JsonResponse
from .serializers import ClassSerializer
from .models import Class

def class_list(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)
    return JsonResponse(serializer.data)