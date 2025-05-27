from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
import uuid

from trips.city import CITY_SENEGAL

DAYS_OF_WEEK = [
    ('monday', 'Lundi'),
    ('tuesday', 'Mardi'),
    ('wednesday', 'Mercredi'),
    ('thursday', 'Jeudi'),
    ('friday', 'Vendredi'),
    ('saturday', 'Samedi'),
    ('sunday', 'Dimanche'),
]


class Homework(models.Model):
    DRIVER = 'driver'
    PASSENGER = 'passenger'

    ROLE_CHOICES = [
        (DRIVER, 'Conducteur'),
        (PASSENGER, 'Passager'),
    ]

    start_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    end_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    price = models.PositiveIntegerField()
    seat_go = models.PositiveIntegerField()
    seat_return = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    premium = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=DRIVER)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # days of the week for the homework
    monday_active = models.BooleanField(default=False, verbose_name="Lundi actif")
    monday_start = models.TimeField(blank=True, null=True, verbose_name="Lundi départ")
    monday_end = models.TimeField(blank=True, null=True, verbose_name="Lundi retour")

    tuesday_active = models.BooleanField(default=False, verbose_name="Mardi actif")
    tuesday_start = models.TimeField(blank=True, null=True, verbose_name="Mardi départ")
    tuesday_end = models.TimeField(blank=True, null=True, verbose_name="Mardi retour")

    wednesday_active = models.BooleanField(default=False, verbose_name="Mercredi actif")
    wednesday_start = models.TimeField(blank=True, null=True, verbose_name="Mercredi départ")
    wednesday_end = models.TimeField(blank=True, null=True, verbose_name="Mercredi retour")

    thursday_active = models.BooleanField(default=False, verbose_name="Jeudi actif")
    thursday_start = models.TimeField(blank=True, null=True, verbose_name="Jeudi départ")
    thursday_end = models.TimeField(blank=True, null=True, verbose_name="Jeudi retour")

    friday_active = models.BooleanField(default=False, verbose_name="Vendredi actif")
    friday_start = models.TimeField(blank=True, null=True, verbose_name="Vendredi départ")
    friday_end = models.TimeField(blank=True, null=True, verbose_name="Vendredi retour")

    saturday_active = models.BooleanField(default=False, verbose_name="Samedi actif")
    saturday_start = models.TimeField(blank=True, null=True, verbose_name="Samedi départ")
    saturday_end = models.TimeField(blank=True, null=True, verbose_name="Samedi retour")

    sunday_active = models.BooleanField(default=False, verbose_name="Dimanche actif")
    sunday_start = models.TimeField(blank=True, null=True, verbose_name="Dimanche départ")
    sunday_end = models.TimeField(blank=True, null=True, verbose_name="Dimanche retour")

    def __str__(self):
        return f"{self.start_city} - {self.end_city}"

    def get_absolute_url(self):
        id_abbr = str(self.id)[:8]
        start_city_slug = slugify(self.start_city)
        end_city_slug = slugify(self.end_city)
        return reverse("homework-detail",
                       kwargs={"start_city_slug": start_city_slug, "end_city_slug": end_city_slug, "id_abbr": id_abbr})

    def get_absolute_url_update(self):
        id_abbr = str(self.id)[:8]
        start_city_slug = slugify(self.start_city)
        end_city_slug = slugify(self.end_city)
        return reverse("homework-update",
                       kwargs={"start_city_slug": start_city_slug, "end_city_slug": end_city_slug, "id_abbr": id_abbr})

    def get_absolute_url_delete(self):
        id_abbr = str(self.id)[:8]
        start_city_slug = slugify(self.start_city)
        end_city_slug = slugify(self.end_city)
        return reverse("homework-delete",
                       kwargs={"start_city_slug": start_city_slug, "end_city_slug": end_city_slug, "id_abbr": id_abbr})


