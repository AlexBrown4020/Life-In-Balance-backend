from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from .serializers import ClassSerializer
from .models import Class
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ClassGetAllView(generics.GenericAPIView):
    def get(self, request):
        sessions = Class.objects.all()
        serializer = ClassSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

class ClassView(generics.GenericAPIView):
    def get(self, request, class_id):
        session = get_object_or_404(Class, pk=class_id)
        serializer = ClassSerializer(session)
        return JsonResponse(serializer.data, safe=False)