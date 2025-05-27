from django.contrib import admin
from .models import Homework
# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'author', 'start_city', 'end_city', 'price', 'seat_go']
    search_fields = ["start_city", "end_city", "price"]
    ordering = ['-created_at']
    list_per_page = 20
    list_filter = ['active', 'premium']

