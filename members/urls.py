from django.urls import path
from members.views import registration_view

app_name = 'members'

urlpatterns = [
    path('register', registration_view, name='register'),
]