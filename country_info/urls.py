from django.urls import path
from country_info import views
urlpatterns = [
    path("", views.get, name="get"),
    path("put/<int:pk>", views.put, name="put"),
]