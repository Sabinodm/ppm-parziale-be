from django.contrib import admin

from django.contrib import admin
from .models import ForecastData

@admin.register(ForecastData)
class ForecastDataAdmin(admin.ModelAdmin):
    list_display = ['location', 'date', 'time', 'result']
    search_fields = ['location']