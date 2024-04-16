from django.contrib import admin
from django.urls import path
from Station import views

urlpatterns = [
    path('station',views.station_function,name="station"),
]
