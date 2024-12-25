from django.urls import path
from . import views

urlpatterns = [
   path('calendar/', views.event_calendar, name='event_calendar'),
]