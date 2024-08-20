from django.contrib import admin
from .models import Covoiturage
# Register your models here.


class CovoiturageAdmin(admin.ModelAdmin):
    list_display = ('author', 'start_city', 'end_city', 'price')
    list_filter = ('author', 'start_city', 'end_city', 'price')
    search_fields = ('author', 'start_city', 'end_city')
    ordering = ('author', 'start_city', 'end_city')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Covoiturage, CovoiturageAdmin)