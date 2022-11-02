from django.contrib import admin
from termsAndConditions import models


@admin.register(models.TermsAndConditions)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id","body")
