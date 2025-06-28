from rest_framework import serializers
from .models import ForecastQuery, ForecastData


class ForecastDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastData
        fields = '__all__'

class ForecastQuerySerializer(serializers.ModelSerializer):
    location = serializers.CharField(write_only=True)
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)

    forecast_data = ForecastDataSerializer(read_only=True)

    class Meta:
        model = ForecastQuery
        fields = ['id', 'user', 'forecast_data', 'created_at',
                  'location', 'date', 'time']
        read_only_fields = ['user', 'forecast_data', 'created_at']
