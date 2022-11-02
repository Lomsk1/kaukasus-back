from django.urls import path
from photoblog.gallery import views
urlpatterns = [
    path("", views.get, name="get"),
    path("<int:pk>/", views.getById, name="GetById"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("post/", views.post, name="post"),
    path("put/<int:pk>/", views.put, name="put")
]