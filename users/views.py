from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # chiunque può registrarsi

@login_required
def fake_payment_view(request):
    user = request.user
    if user.is_premium:
        return render(request, "users/already_premium.html", {"user": user})

    if request.method == "POST":
        user = request.user
        user.is_premium = True
        user.save()
        return render(request, "users/payment_success.html")

    return render(request, "users/fake_payment.html")