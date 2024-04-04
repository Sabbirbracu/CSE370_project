from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base',views.base,name="base"),
    path('',views.index,name='index'),
    path('login', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register',views.register,name='register'),
]
