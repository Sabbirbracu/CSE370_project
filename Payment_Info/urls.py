from django.contrib import admin
from django.urls import path
from Payment_Info import views

urlpatterns = [
    path('payment',views.payment,name="payment"),
]