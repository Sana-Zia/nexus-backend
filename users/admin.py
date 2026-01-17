from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role', 'bio', 'startup_info', 'investment_info')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')

admin.site.register(User, UserAdmin)
