from django.urls import path
from tours.services import views

urlpatterns = [
    path("all/", views.get, name="get"),
    path("<int:pk>/", views.getById, name="getById"),
    path("post/", views.post, name="post"),
    path("put/<int:pk>/", views.put, name="put"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]