from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('payment',views.payment_info,name="payment"),
]