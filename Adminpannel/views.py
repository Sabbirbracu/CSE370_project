
from django.shortcuts import render,redirect
from Bike_Station.models import Bike_Station

# Create your views here.
def admin_dashboard(request):
    page = "admin_dashboard"
    return render(request,"admin_home/admin_dashboard.html",{'page':page})

def update_station(request):
    page = "update_station"
    return render(request,"admin_home/update_station.html",{'page':page})

def insert_station(request):
    if request.method == "POST":
        station_name = request.POST.get('station_name')
        num_of_bikes = request.POST.get('num_of_bikes')
        station_status = request.POST.get('status')

        station = Bike_Station(Station_Name=station_name,Number_of_Bikes=num_of_bikes,Station_Status=station_status)
        station.save()
        return redirect("bikestation")
    page = "insert_station"
    return render(request,"admin_home/insert_station.html",{'page':page})