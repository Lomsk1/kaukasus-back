from django.db import models

class TermsAndConditions(models.Model):
    body = models.TextField(blank=True, default="terms and conditions")