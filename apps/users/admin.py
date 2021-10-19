from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = ("email", "username", "first_name", "last_name")
    list_display = ("email", "username", "first_name", "last_name", "is_active", "is_staff")
    ordering = ("email", "username", "first_name", "last_name")
    list_filter = ("email", "username", "first_name", "last_name", "is_active", "is_staff")
    fieldsets = (
        ("Credential", {"fields": ("email", "username", "first_name", "last_name", "other_names", "date_of_birth")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Personal info", {"fields": ("about",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "other_names",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
