from django.db import models
from django.conf import settings
import uuid
from covoiturages.city import CITY_SENEGAL
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Covoiturage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    end_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    monday_departure = models.TimeField(blank=True, null=True)
    monday_return = models.TimeField(blank=True, null=True)
    tuesday_departure = models.TimeField(blank=True, null=True)
    tuesday_return = models.TimeField(blank=True, null=True)
    wednesday_departure = models.TimeField(blank=True, null=True)
    wednesday_return = models.TimeField(blank=True, null=True)
    thursday_departure = models.TimeField(blank=True, null=True)
    thursday_return = models.TimeField(blank=True, null=True)
    friday_departure = models.TimeField(blank=True, null=True)
    friday_return = models.TimeField(blank=True, null=True)
    saturday_departure = models.TimeField(blank=True, null=True)
    saturday_return = models.TimeField(blank=True, null=True)
    sunday_departure = models.TimeField(blank=True, null=True)
    sunday_return = models.TimeField(blank=True, null=True)
    seat_go = models.PositiveIntegerField()
    seat_back = models.PositiveIntegerField(default=0, blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    return_trip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"Covoiturage régulier de {self.start_city} à {self.end_city} - {self.author}"


    def get_absolute_url(self):
        id_abbr = str(self.id)[:8]
        start_city_slug = slugify(self.start_city)
        end_city_slug = slugify(self.end_city)
        return reverse("covoiturage_detail",
                       kwargs={"start_city_slug": start_city_slug, "end_city_slug": end_city_slug, "id_abbr": id_abbr})

    def get_absolute_url_update(self):
        return reverse("covoiturage_update", kwargs={"pk": self.pk})

    def get_absolute_url_delete(self):
        return reverse("covoiturage_delete", kwargs={"pk": self.pk})
