from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ride/', views.ride, name="ride"),  # Ensure the trailing slash '/'
    path('ride_time/', views.ride_time, name="ride_time"),  # Ensure the trailing slash '/'
    path('stop_ride/', views.stop_ride, name='stop_ride'),  # Add this line
]
