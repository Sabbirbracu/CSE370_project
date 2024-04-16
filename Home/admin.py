# Inside Home/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    pass  # You can customize the display of user fields here if needed

admin.site.register(CustomUser, CustomUserAdmin)
