from django.urls import path
from . import views
from views import *

app_name = 'members'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('members/', views.GetMembers.as_view(), name='members'),
]