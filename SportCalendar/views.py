from django.shortcuts import render
from .models import Event
from django.db.models import Prefetch

def event_calendar(request):
    events = Event.objects.select_related('club').prefetch_related('disciplines').order_by('date_start')
    context = {'events': events}
    return render(request, 'SportCalendar.html', context)