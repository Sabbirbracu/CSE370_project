from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Ride,CustomUser,Bike_Station
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
@never_cache

def ride(request):
    if request.method == 'POST':
        # Assuming the input fields have names 'box1' and 'box2' in the form
        start_dest = request.POST.get('start_destination')
        end_dest = request.POST.get('end_destination')
        # start_station = get_object_or_404(Bike_Station, Station_Name=start_dest)
        start_station = Bike_Station.objects.get(Station_Name=start_dest)
        get_station_id = start_station.pk
        user_id = request.user.id

        # Check if both boxes have the same input
        if start_dest == end_dest:
            # Return an error response
            messages.error(request, 'Please enter different destinations')

        else:
            station_id = Bike_Station.objects.get(Station_ID=get_station_id)
            ride = Ride(station_name=start_dest, destination=end_dest,user_id=user_id,station=station_id)
            ride.save()
            return redirect("ride_time")

    stations = Bike_Station.objects.all()
    page = "ride"
    return render(request,'ride/ride.html',{'page':page,'stations':stations})


def ride_time(request):
    if request.method == 'POST':
        elapsed_time = request.POST.get('elapsedTime')
        latest_ride = Ride.objects.latest('ride_id')
        latest_ride.total_time=elapsed_time
        latest_ride.save()
        
    
    page = "ride_time"
    return render(request,'ride/ride_time.html',{'page':page})