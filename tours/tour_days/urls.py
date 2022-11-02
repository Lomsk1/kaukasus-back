from django.urls import path
from tours.tour_days import views

urlpatterns = [
    path("all/<int:tour_id>/", views.getTourDays, name="getTourDays"),
    path("<int:day_id>/", views.getTourDaysById, name="getTourDays"),
    path("delete/<int:day_id>/", views.deleteTourDay, name="deleteTourDay"),
    path("post/", views.postTourDay, name="postTourDay"),
    path("put/<int:day_id>/", views.putTourDay, name="putTourDay")
]