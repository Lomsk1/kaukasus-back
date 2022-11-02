from django.urls import path
from tours.tour import views

urlpatterns = [
    path("all/", views.getTour, name="getTours"),
    path("<int:pk>/", views.getTourById, name="getTour"),
    path("post/", views.postTour, name="post"),
    path("put/<int:pk>/", views.putTour, name="putTour"),
    path("delete/<int:pk>/", views.deleteTour, name="deleteTour"),
    path("<str:country>/", views.getTourByCountry, name="getTourByCountry"),
]