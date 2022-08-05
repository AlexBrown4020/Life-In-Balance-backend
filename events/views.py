from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class EventGetAllView(generics.GenericAPIView):
    def get(self, request):
        sessions = Event.objects.all()
        serializer = EventSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

class SessionView(generics.GenericAPIView):
    def get(self, request, session_id):
        session = get_object_or_404(Event, pk=session_id)
        serializer = EventSerializer(session)
        return JsonResponse(serializer.data, safe=False)

class CreateSessionView(generics.GenericAPIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)