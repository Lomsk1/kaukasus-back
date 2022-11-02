from django.urls import path
from tours.comments import views
urlpatterns = [
    path("get/", views.get, name="get"),
    path("get/<int:pk>/", views.getById, name="get"),
    path("get/tour/<int:tour_id>/", views.getByTour, name="getByTour"),
    path("post/", views.post, name="post"),
    path("put/<int:pk>/", views.put, name="put"),
    path("delete/<int:pk>/", views.delete, name="delete")
]