from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = ("email", "username", "first_name", "last_name")
    list_display = ("email", "username", "first_name", "last_name", "is_active", "is_staff")
    ordering = ("email", "username", "first_name", "last_name")
    list_filter = ("email", "username", "first_name", "last_name", "is_active", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
