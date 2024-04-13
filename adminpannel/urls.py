from django.contrib import admin
from django.urls import path
from adminpannel import views

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('update_station',views.update_station,name="update_station"),

]
