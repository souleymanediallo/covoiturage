from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from cities.sitemaps import CitySitemap, StaticViewSitemap

from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'cities': CitySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("trajets/", include("trips.urls")),
    path("trajets-reguliers/", include("covoiturages.urls")),
    path("cars/", include("cars.urls")),
    path("conversations/", include("conversations.urls")),
    path("contact/", include("contact.urls")),
    path("destination/", include("cities.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)