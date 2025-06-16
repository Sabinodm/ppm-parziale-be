from rest_framework import serializers
from .models import ForecastQuery

class ForecastQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastQuery
        fields = '__all__'
        read_only_fields = ['user', 'result', 'created_at']
