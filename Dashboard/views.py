from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from MakeRide.models import Ride



@login_required
@never_cache

def dashboard(requests):
    
    rides = Ride.objects.filter(user=requests.user)
    
    context = {
        'rides': rides,
        'page': "dashboard"
    }
    return render(requests,'Dashboard/dashboard.html', context)
