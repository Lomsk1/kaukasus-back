from django.urls import path
from tours.highlights import views

urlpatterns = [
    path("all/<int:tour_id>/", views.getHighlights, name="getHighlights"),
    path("<int:highlight_id>/", views.getHighlightsById, name="highlight_id"),
    path("delete/<int:highlight_id>/", views.delete, name="deleteHighlight"),
    path("post/", views.post, name="postHighlight"),
    path("put/<int:pk>/", views.put, name="putHighlight")
]