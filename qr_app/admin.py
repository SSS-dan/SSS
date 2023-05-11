from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

@admin.register(models.NewUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "username",
                )
            },
        ),
    )
    list_display = (
        "username",
        "is_active",
        "is_staff",
    )