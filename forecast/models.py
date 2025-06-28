from django.db import models
from django.conf import settings

class ForecastData(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    result = models.TextField()

    def __str__(self):
        return f"{self.location} {self.date} {self.time} → {self.result}"


class ForecastQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forecast_data = models.ForeignKey(ForecastData, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.forecast_data} - {self.created_at}"
