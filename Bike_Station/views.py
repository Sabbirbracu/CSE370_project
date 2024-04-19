from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Bike_Station


@login_required
@never_cache

def bikestation(requests):
    bikestations = Bike_Station.objects.all()
    context = {
        'bikestations': bikestations,
        'page': "bikestation"
    }
    return render(requests,'bikestation_html/bikestation.html', context)