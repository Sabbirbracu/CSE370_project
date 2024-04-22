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


# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Ride
from datetime import datetime, timedelta
def ride_time(request):
    latest_ride = Ride.objects.latest('ride_id')
    return render(request, 'ride/timer.html', {'ride': latest_ride})

def stop_ride(request):
    if request.method == 'POST':
        ride_id = request.POST.get('ride_id')
        elapsed_time = request.POST.get('elapsed_time')
        
        # Convert elapsed time to minutes
        hh, mm, ss = elapsed_time.split(':')
        total_minutes = int(hh) * 60 + int(mm)

        ride = Ride.objects.get(pk=ride_id)
        print(total_minutes)
        ride.total_time = total_minutes
        ride.save()

        # Redirect to the payment page
        return redirect('payment')  # Replace 'payment' with the actual URL name for your payment page

    return JsonResponse({'success': False})
