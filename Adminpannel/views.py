
from django.shortcuts import render,redirect
from Bike_Station.models import Bike_Station
from Home.models import CustomUser
from MakeRide.models import Ride
from django.shortcuts import get_object_or_404
from django.db import connection
from django.db.models import Count


# Create your views here.
def admin_dashboard(request):
    # total_stations = Bike_Station.objects.count()
    # total_ride_users = CustomUser.objects.filter(user_type='Rider').count()

    top_stations = (
        Ride.objects.values('station_name')
                    .annotate(total_rides=Count('ride_id'))
                    .order_by('-total_rides')[:2]
    )
        
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Bike_Station")
        total_stations = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Home_customuser WHERE user_type = 'Rider'")
        total_ride_users = cursor.fetchone()[0]


    ride_history = Ride.objects.values('station_name', 'ride_id', 'destination')

    page = "admin_dashboard"
    return render(request, "admin_home/admin_dashboard.html", {'page': page, 'total_stations': total_stations, 
                                                               'total_ride_users': total_ride_users,'top_stations': top_stations,'ride_history':ride_history})

def update_station(request):
    bikestations = Bike_Station.objects.all()
    page = "update_station"
    return render(request,"admin_home/update_station.html",{'page':page,'bikestations':bikestations})

def insert_station(request):
    if request.method == "POST":
        station_name = request.POST.get('station_name')
        num_of_bikes = request.POST.get('num_of_bikes')
        if int(num_of_bikes) < 1:    
            station_status = "Unavailable"
        else:
            station_status = "Available"

        station = Bike_Station(Station_Name=station_name,Number_of_Bikes=num_of_bikes,Station_Status=station_status)
        station.save()
        return redirect("bikestation")
    page = "insert_station"
    return render(request,"admin_home/insert_station.html",{'page':page})

def edit_station(request,pk):
    station = Bike_Station.objects.get(Station_ID=pk)
    # station = get_object_or_404(Bike_Station, Station_ID=pk)
    # we can do this with two systems

    if request.method == "POST":
        station_name = request.POST.get('station_name')
        num_of_bikes = request.POST.get('num_of_bikes')
        if int(num_of_bikes) < 1:
            station_status = 'Unavailable'
        else:
            station_status = 'Available'

        station.Station_Name = station_name
        station.Number_of_Bikes = num_of_bikes
        station.Station_Status = station_status
        station.save()
        return redirect("bikestation")
    
    page = "edit_station"
    return render(request,"admin_home/edit_station.html",{'page':page,'station':station})


def view_users(request):
    Users = CustomUser.objects.all()
    page = "view_users"
    return render(request,"admin_home/view_users.html",{'page':page,'Users':Users})


def delete_station(request,pk):
    station = Bike_Station.objects.get(Station_ID=pk)
    if request.method == "POST":
        station.delete()
        return redirect("bikestation")

    return render(request,"admin_home/delete.html",{'station':station})