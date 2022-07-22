from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.ClassGetAllView.as_view(), name='classes'),
    path('classes/<int:class_id>/', views.ClassView.as_view(), name='class'),
]