from django.urls import path
from .views import RegisterView, fake_payment_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('payment/', fake_payment_view, name='fake-payment')
]