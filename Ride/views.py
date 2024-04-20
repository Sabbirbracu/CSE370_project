from django.shortcuts import render,redirect
from django.contrib import messages
from Ride.models import Ride_data


# Create your views here.

def ride(request):
    if request.method == 'POST':
        # Assuming the input fields have names 'box1' and 'box2' in the form
        start_dest = request.POST.get('start_destination')
        end_dest = request.POST.get('end_destination')


        # Check if both boxes have the same input
        if start_dest == end_dest:
            # Return an error response
            messages.error(request, 'Please enter different destinations')

        else:
            ride = Ride_data(station=start_dest, destination=end_dest)
            ride.save()
            return redirect("ride_time")


    page = "ride"
    return render(request,'ride/ride.html',{'page':page})


def ride_time(request):
    if request.method == 'POST':
        elapsed_time = request.POST.get('elapsedTime')
        latest_ride = Ride_data.objects.latest('ride_id')
        latest_ride.total_time=elapsed_time
        latest_ride.save()
        
    
    page = "ride_time"
    return render(request,'ride/ride_time.html',{'page':page})



