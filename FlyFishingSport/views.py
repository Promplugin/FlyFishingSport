from django.shortcuts import render, redirect
from .models import SiteSettings
from SportCalendar.models import Event
from django.utils import timezone

def some_view(request):
    site_settings = SiteSettings.objects.first()
    logo_url = site_settings.logo.url if site_settings and site_settings.logo else None
    return render(request, 'base.html', {'logo_url': logo_url})

def index(request):
    upcoming_events = Event.objects.filter(date_start__gte=timezone.now()).order_by('date_start')[:5]
    return render(request, 'index.html', {'upcoming_events': upcoming_events})

def contact_view(request):
    return render(request, 'contact.html')