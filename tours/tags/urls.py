from django.urls import path
from tours.tags import views


urlpatterns = [
    path("get/", views.get, name="get"),
    path("get/<int:pk>/", views.getById, name="getById"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("post/", views.post, name="post"),
    path("put/<int:pk>/", views.put, name="put"),
]