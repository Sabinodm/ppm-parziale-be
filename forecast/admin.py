from django.contrib import admin

from django.contrib import admin

from users.models import CustomUser
from .models import ForecastData, ForecastQuery


@admin.register(ForecastData)
class ForecastDataAdmin(admin.ModelAdmin):
    list_display = ['location', 'date', 'time', 'result']
    search_fields = ['location']

@admin.register(ForecastQuery)
class ForecastQueryAdmin(admin.ModelAdmin):
    list_display = ['user', 'forecast_data', 'created_at']
    search_fields = ['user__username', 'forecast_data__location']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

    def has_add_permission(self, request):
        return False

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_premium']
    search_fields = ['username', 'email']
    list_filter = ['is_premium']

    def has_add_permission(self, request):
        return False