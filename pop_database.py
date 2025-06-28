# script to populate database

from forecast.models import ForecastData
from datetime import date, time, timedelta
import random

start_date = date(2025, 6, 28)
end_date = date(2025, 7, 9)
hours = list(range(0, 24))

weather_samples = [
    "Soleggiato",
    "Parzialmente nuvoloso",
    "Nuvoloso",
    "Pioggia leggera",
    "Temporale",
    "Sereno",
    "Nebbia",
    "Vento moderato",
    "Pioggia forte",
    "Umido"
]
try:
    current_date = start_date
    while current_date <= end_date:
        for h in hours:
            random_result = weather_samples[(h + current_date.day) % len(weather_samples)]
            ForecastData.objects.create(
                location="Firenze",
                date=current_date,
                time=time(hour=h, minute=0),
                temp=round(random.uniform(-2, 40), 1),
                result=random_result
            )
        current_date += timedelta(days=1)
finally:
    print("Previsioni create con successo.")
