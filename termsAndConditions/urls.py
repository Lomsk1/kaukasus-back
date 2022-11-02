from django.urls import path
from termsAndConditions import views
urlpatterns = [
    path("", views.get, name="get"),
    path("put/<int:pk>/", views.put, name="put"),
]