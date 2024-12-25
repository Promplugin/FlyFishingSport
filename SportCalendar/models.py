from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    city = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    disciplines = models.ManyToManyField(Discipline)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    link = models.URLField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.name