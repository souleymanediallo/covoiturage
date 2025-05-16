from django.contrib import admin
from .models import Trip, Reservation, Car

# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'author', 'role', 'trip_type', 'start_date', 'start_city', 'end_city', 'price', 'seat_go']
    search_fields = ["start_city", "end_city", "price", "start_date"]
    ordering = ['-created_at']
    list_per_page = 20



