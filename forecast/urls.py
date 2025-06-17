from django.urls import path
from .views import ForecastCreateView, ForecastHistoryView

urlpatterns = [
    path('forecast/', ForecastCreateView.as_view(), name='forecast'),
    path('forecast/history/', ForecastHistoryView.as_view(), name='forecast-history'),
]