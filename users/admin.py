from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_premium']
    search_fields = ['username', 'email']
    list_filter = ['is_premium']

    def has_add_permission(self, request):
        return False
