from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view_profile',views.viewprofile,name="view_profile"),
    path('edit_profile',views.editprofile,name="edit_profile"),
]