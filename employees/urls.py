from django.urls import path
from employees import views


urlpatterns = [
    path("all/", views.get, name="get"),
    path("<int:pk>/", views.byid, name="get_by_id"),
    path("post/", views.post, name="post"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("put/<int:pk>/", views.put, name="put")
]