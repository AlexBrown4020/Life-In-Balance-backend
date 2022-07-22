from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.ClassGetAllView.as_view(), name='classes'),
]