from django.db import models
from django.conf import settings
import uuid
from city import CITY_SENEGAL
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Annonce(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    end_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    seat_go = models.PositiveIntegerField()
    seat_back = models.PositiveIntegerField(default=0, blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    return_trip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"Annonce de {self.start_city} à {self.end_city} - {self.author}"






