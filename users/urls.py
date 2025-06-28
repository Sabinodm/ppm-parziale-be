from django.urls import path
from .views import RegisterView, payment_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('payment/', payment_view, name='fake-payment')
]