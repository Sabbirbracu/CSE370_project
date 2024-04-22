from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',include('Rewards.urls')),
    path('dashboard',views.dashboard,name="dashboard"),
]
