from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid
from .brand import CAR_BRAND, COLOR_CHOICES


# Create your models here.
class Car(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100, choices=CAR_BRAND)
    model = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})

    def get_absolute_url_update(self):
        return reverse("car_update", kwargs={"pk": self.pk})

    def get_absolute_url_delete(self):
        return reverse("car_delete", kwargs={"pk": self.pk})