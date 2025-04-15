from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('country', 'city', 'phone_number', 'day_of_birth', 'address')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('country', 'city', 'phone_number', 'day_of_birth', 'address')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
