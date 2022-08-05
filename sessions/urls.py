from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.ClassGetAllView.as_view(), name='sessions'),
    path('sessions/<int:session_id>/', views.ClassView.as_view(), name='session'),
]