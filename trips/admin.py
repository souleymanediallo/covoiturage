from django.contrib import admin
from .models import Trip, Reservation, Car
# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['start_city', 'end_city', 'price', 'start_date', 'seat_go',  'created_at']
    search_fields = ["start_city", "end_city", "price", "start_date"]

