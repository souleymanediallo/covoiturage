from django.db import models
from django.conf import settings
import uuid
from django.db.models import Count
from django.db.models import Sum
from cars.models import Car
from django.urls import reverse
from .city import CITY_SENEGAL


# Create your models here.
class Trip(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='trips', null=True)
    start_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    end_city = models.CharField(max_length=100, choices=CITY_SENEGAL)
    start_date = models.DateField()
    start_time = models.TimeField()
    seat_go = models.PositiveIntegerField()
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
        return f"{self.start_city} - {self.end_city}"

    @classmethod
    def get_popular_cities(cls):
        return cls.objects.values('start_city').annotate(count=Count('start_city')).order_by('-count')[:5]

    def get_absolute_url(self):
        return reverse("trip-detail", kwargs={"pk": self.pk})

    def get_absolute_url_update(self):
        return reverse("trip-update", kwargs={"pk": self.pk})

    def get_absolute_url_delete(self):
        return reverse("trip-delete", kwargs={"pk": self.pk})


class Reservation(models.Model):
    PENDING = 'En attente'
    ACCEPTED = 'Acceptée'
    REFUSED = 'Refusée'
    CANCELLED = 'Annulée'

    STATUS_CHOICES = [
        (PENDING, 'En attente'),
        (ACCEPTED, 'Acceptée'),
        (REFUSED, 'Refusée'),
        (CANCELLED, 'Annulée'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reservations')
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seats_reserved_go = models.PositiveIntegerField()
    seats_reserved_back = models.PositiveIntegerField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Réservation par {self.passenger} pour {self.seats_reserved_go} places"

    def accept(self):
        self.status = self.ACCEPTED
        self.save()

    def refuse(self):
        self.status = self.REFUSED
        self.save()

    def cancel(self):
        self.status = self.CANCELLED
        self.save()