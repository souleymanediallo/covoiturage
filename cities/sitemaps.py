from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import City


class CitySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return City.objects.all()

    def location(self, obj):
        return reverse('city-detail', args=[obj.slug])


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['home', 'contact']

    def location(self, item):
        return reverse(item)