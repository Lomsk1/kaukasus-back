from django.db import models
import os


class Tags(models.Model):
    name = models.CharField(max_length=255, null=False, )
    def __str__(self):
        return self.name


class Tour(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, related_name="tag")
    title = models.CharField(max_length=255, null=False)
    abstract_price = models.IntegerField()
    duration = models.IntegerField()
    countryName = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    minParticipants = models.IntegerField(blank=False)
    maxParticipants = models.IntegerField(blank=False)
    execution = models.CharField(max_length=100, null=False, blank=True, default="Guaranteed")
    language = models.CharField(max_length=100, null=False, blank=True, default="Deutsch")
    image = models.ImageField(upload_to="./tours", default="./tours/tour_default.jpg")
    def __str__(self):
        return self.countryName + " - " + self.title


class Services(models.Model):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, blank=True)
    notedAchievements = models.TextField(null=False, blank=True)
    servicesNotRealized = models.TextField(null=False, blank=True)


class TourDays(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, related_name="tour_days")
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="./tour_days", default="./tour_days/tour-days_default.jpg")
    drivingKilometers = models.IntegerField()
    driveTime = models.IntegerField()
    meals = models.TextField(default="")
    overnight_stay = models.CharField(max_length=255, null=True)

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    startDate = models.DateField(null=False, blank=False)
    endDate = models.DateField(null=False, blank=False)
    price = models.IntegerField()
    booking_remaining_places_img = models.ImageField(upload_to="./booking", default="./booking/booking_default.png")

    def __str__(self):
        return self.tour.__str__() + " | " +"Booking"


class Comments(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    body = models.TextField()
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)


class Highlight(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    highlight = models.CharField(max_length=100, blank=False)


class SingleRoom(models.Model):
    description = models.TextField(blank=True)


def img_delete(image, *args, **kwargs):
    if os.path.isfile(image):
        img_path = os.path.join("kauk/home/nika/Documents/projects/python/snakeasus-api", image)
        img_path = os.path.abspath(img_path)
        os.remove(img_path)


