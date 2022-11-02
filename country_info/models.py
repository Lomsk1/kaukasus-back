from django.db import models

class CountryInfo(models.Model):
    country_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
