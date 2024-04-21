from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ride',views.ride,name="ride"),
    path('ride_time',views.ride_time,name="ride_time"),
]
