import random
from rest_framework import generics, permissions
from .models import ForecastQuery
from .serializers import ForecastQuerySerializer
from rest_framework.exceptions import PermissionDenied
from django.utils.timezone import localdate

class ForecastCreateView(generics.CreateAPIView):
    queryset = ForecastQuery.objects.all()
    serializer_class = ForecastQuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_premium:
            today = localdate()
            count_today = ForecastQuery.objects.filter(user=user, created_at__date=today).count()
            if count_today >= 10:
                raise PermissionDenied("Hai raggiunto il limite giornaliero di 10 richieste.")

        fake_result = random.choice(["Soleggiato 25°C", "Pioggia 18°C", "Neve -2°C"])
        serializer.save(user=user, result=fake_result)