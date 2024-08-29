from django.contrib import admin
from .models import City
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CityAdmin)

