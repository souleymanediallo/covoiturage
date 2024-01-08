from django.contrib import admin
from .models import CustomUser, Profile
from django.utils.html import format_html
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'user_type', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')})
    )
    list_display = ['first_name', 'email', 'last_name', 'user_type', 'phone_number', 'date_joined', 'last_login']
    search_fields = ["email", "first_name", "last_name", "user_type", "phone_number"]

    filter_horizontal = ()
    list_filter = ()
    Fieldsets = ()


class ProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%;">'.format(object.image.url))

    def user_info(self, object):
        return f'{object.user.user_type}, {object.user.phone_number}, {object.user.user_type}, {object.user.last_login}'

    list_display = ['thumbnail', 'user', 'user_info']


admin.site.register(Profile, ProfileAdmin)