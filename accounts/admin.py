from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_guest', 'is_staff', 'date_joined')
    list_filter = ('is_guest', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('avatar', 'bio', 'is_guest')}),
    )
