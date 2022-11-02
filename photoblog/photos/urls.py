from django.urls import path
from photoblog.photos import views

urlpatterns = [
    path("all/", views.get, name="get"),
    path("all/<int:gallery_pk>/", views.getAllPhotosById, name="GetPhotosWithGalleryPK"),
    path("<int:pk>/", views.byid, name="byid"),
    path("post/", views.post, name="post"),
    path("put/<int:pk>/", views.put, name="put"),
    path("delete/<int:pk>/", views.delete, name="delete")
]