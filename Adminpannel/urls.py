from django.contrib import admin
from django.urls import path
from Adminpannel import views

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('update_station',views.update_station,name="update_station"),
    path('insert_station',views.insert_station,name="insert_station"),
    path('view_users',views.view_users,name="view_users"),
    path('edit_station/<int:pk>',views.edit_station,name="edit_station"),
    path('delete_station/<int:pk>',views.delete_station,name="delete_station"),

]