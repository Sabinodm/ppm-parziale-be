from rest_framework import serializers
from .models import ForecastQuery, ForecastData


class ForecastDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastData
        fields = '__all__'

class ForecastQuerySerializer(serializers.ModelSerializer):
    forecast_data = ForecastDataSerializer(read_only=True)

    class Meta:
        model = ForecastQuery
        fields = ['id', 'user', 'forecast_data', 'created_at']
        read_only_fields = ['user', 'forecast_data', 'created_at']
