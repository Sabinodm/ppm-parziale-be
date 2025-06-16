from django.urls import path
from .views import ForecastCreateView

urlpatterns = [
    path('forecast/', ForecastCreateView.as_view(), name='forecast'),
]