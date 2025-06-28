from django.db import models
from django.conf import settings
from datetime import time

class ForecastData(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    TIME_CHOICES = [(time(h, 0), f"{h:02d}") for h in range(0, 24)]
    time = models.TimeField(choices=TIME_CHOICES)
    result = models.TextField()

    def __str__(self):
        return f"{self.location} {self.date} {self.time} → {self.result}"


class ForecastQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    forecast_data = models.ForeignKey(ForecastData, on_delete=models.SET_NULL, null=True)
    session_id = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.forecast_data} - {self.created_at}"
        return f" session: {self.session_id} - {self.forecast_data} - {self.created_at}"
