from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base,name="base"),
    path('',views.index,name='index'),
    path('login',views.login_view,name="login"),
    path('register',views.register,name='register'),
]
