from django.urls import path
from tours.filters import views
urlpatterns = [
    path("<int:tag_id>/", views.filterTourByTag, name="filterTourByTag"),
    path("datefilter/", views.filterByDate, name="filterToursByDate")
]