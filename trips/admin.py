from django.contrib import admin
from .models import Trip, Reservation, Car
# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['start_city', 'end_city', 'price', 'start_date', 'seat_go', 'seat_back', 'end_date', 'created_at']
    search_fields = ["start_city", "end_city", "price", "start_date", "end_date"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['status', 'seats_reserved_go', 'seats_reserved_back', 'created_at']


