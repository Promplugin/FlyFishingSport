from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Club, Discipline, Event

admin.site.register(Club)
admin.site.register(Discipline)
admin.site.register(Event)