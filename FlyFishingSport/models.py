from django.db import models

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return "Site Settings"