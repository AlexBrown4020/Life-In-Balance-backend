from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventGetAllView.as_view(), name='events'),
    path('events/<int:event_id>/', views.EventView.as_view(), name='events'),
    path('events/create/', views.CreateEventView.as_view(), name='create_event'),
]