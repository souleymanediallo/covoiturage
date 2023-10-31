from django.contrib import admin
from .models import CustomUser, Profile
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'user_type', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')})
    )
    list_display = ['email', 'first_name', 'last_name', 'user_type', 'phone_number', 'date_joined', 'last_login']
    search_fields = ["email", "first_name", "last_name", "user_type", "phone_number"]


admin.site.register(Profile)
