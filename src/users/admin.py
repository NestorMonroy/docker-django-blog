"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from src.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


"""se sobre escribe el nuevo admin """
admin.site.register(User, CustomUserAdmin)
