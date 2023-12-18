from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# admin.site.register(UserAdmin)


class CustomUserAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


admin.site.register(CustomUser, CustomUserAdmin)
