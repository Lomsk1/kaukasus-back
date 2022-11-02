from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import country_info.apps

schema_view = get_schema_view(
   openapi.Info(
      title="kaukasus api",
      default_version='v1',
      description="API for company Kaukasus Travel which provides tours to Georgia, Azerbaijan and Armenia",
   ),
   public=True,
   permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('employees/', include("employees.urls"), name='employess'),

    path("photo-blog/", include("photoblog.photos.urls"), name='photoblog'),
    path("gallery/", include("photoblog.gallery.urls"), name="gallery"),

    path("auth/", include("authUser.urls")),


    path("tours/", include("tours.tour.urls")),
    path("tour_days/", include("tours.tour_days.urls")),
    path("filters/", include("tours.filters.urls")),
    path("tag/", include("tours.tags.urls")),
    path("booking/", include("tours.booking.urls")),
    path("comments/", include("tours.comments.urls")),
    path("services/", include("tours.services.urls")),
    path("highlights/", include("tours.highlights.urls")),

    path("terms/", include("termsAndConditions.urls")),

    path("country_info/", include("country_info.urls")),

    path("single_room/", include("tours.single_room.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^images/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]