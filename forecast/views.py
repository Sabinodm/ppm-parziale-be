from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import ForecastQuery, ForecastData
from .serializers import ForecastQuerySerializer
from rest_framework.exceptions import PermissionDenied
from django.utils.timezone import localdate

class ForecastCreateView(generics.CreateAPIView):
    serializer_class = ForecastQuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        location = data.get("location")
        date = data.get("date")
        time = data.get("time")

        if not user.is_premium:
            today = localdate()
            count_today = ForecastQuery.objects.filter(user=user, created_at__date=today).count()
            if count_today >= 10:
                raise PermissionDenied("Hai raggiunto il limite giornaliero di 10 richieste.")

        try:
            forecast_data = ForecastData.objects.get(location=location, date=date, time=time)
        except ForecastData.DoesNotExist:
            return Response({"error": "Previsione non trovata nel database."}, status=404)

        forecast_query = ForecastQuery.objects.create(user=user, forecast_data=forecast_data)
        serializer = self.get_serializer(forecast_query)
        return Response(serializer.data)

class ForecastHistoryView(generics.ListAPIView):
    serializer_class = ForecastQuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_premium:
            raise PermissionDenied("Solo gli utenti premium possono vedere lo storico delle previsioni.")
        return ForecastQuery.objects.filter(user=user).order_by('-created_at')