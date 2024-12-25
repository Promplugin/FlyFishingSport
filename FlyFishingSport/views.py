from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import SiteSettings

def some_view(request):
    site_settings = SiteSettings.objects.first()
    logo_url = site_settings.logo.url if site_settings and site_settings.logo else None
    return render(request, 'base.html', {'logo_url': logo_url})

def index(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')