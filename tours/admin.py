from django.contrib import admin
from tours import models


admin.site.register(models.Tour)
admin.site.register(models.TourDays)
admin.site.register(models.Tags)
admin.site.register(models.Booking)
admin.site.register(models.Comments)
admin.site.register(models.Services)
admin.site.register(models.Highlight)
admin.site.register(models.SingleRoom)