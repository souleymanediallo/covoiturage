from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("trajets-ponctuels/", include("trips.urls")),
    path("trajets-reguliers/", include("covoiturages.urls")),
    path("cars/", include("cars.urls")),
    path("conversations/", include("conversations.urls")),
    path("contact/", include("contact.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)