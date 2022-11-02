from django.contrib import admin
from country_info import models
@admin.register(models.CountryInfo)
class AdminCountryInfo(admin.ModelAdmin):
    list_display = ["id","country_name" ,  "title", "description"]