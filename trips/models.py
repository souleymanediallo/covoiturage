from django.db import models
from django.conf import settings
import uuid

from django.db.models import Sum

from django.urls import reverse
from .city import CITY_SENEGAL


# Create your models here.
class Trip(models.Model):
    TRIP_TYPE = (
        ('Aller Simple', 'Aller Simple'),
        ('Aller Retour', 'Aller Retour')
    )
    USER_TYPE = (
        ('Conducteur', 'Conducteur'),
        ('Passager', 'Passager')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='Conducteur')
    trip_type = models.CharField(max_length=20, choices=TRIP_TYPE, default='Aller Simple')
    start_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    end_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    seat_go = models.PositiveIntegerField()
    seat_back = models.PositiveIntegerField(blank=True, null=True)
    luggage = models.PositiveIntegerField(default=0, blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    premium = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_city', 'end_city']

    def __str__(self):
        return f"{self.start_date} - {self.start_city}"
