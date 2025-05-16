from django.contrib import admin
from .models import Stop, BusLine, BusStop
# Register your models here.


class StopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

class BusLineAdmin(admin.ModelAdmin):
    list_display = ('number', 'departure', 'arrival')
    search_fields = ('number', 'departure', 'arrival')
    list_per_page = 20


class BusStopAdmin(admin.ModelAdmin):
    list_display = ('line', 'stop', 'order')
    search_fields = ('line__number', 'stop__name')
    list_per_page = 20


admin.site.register(Stop, StopAdmin)
admin.site.register(BusLine, BusLineAdmin)
admin.site.register(BusStop, BusStopAdmin)