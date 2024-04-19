from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@login_required
@never_cache

def ride(requests):
    page = "ride"
    return render(requests,'Ride/ride.html', {'page':page})