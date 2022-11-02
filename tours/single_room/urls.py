from django.urls import path
from tours.single_room import views
urlpatterns = [
    path("", views.get, name="get"),
    path("put/<int:pk>/", views.put, name="put"),
]