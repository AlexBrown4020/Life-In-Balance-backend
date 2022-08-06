from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from members.serializers import UserCreationSerializer
from .models import Member
# Create your views here.
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserCreationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user."
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

class GetMembers(generics.GenericAPIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)