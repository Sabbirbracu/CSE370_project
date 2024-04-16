from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Station_data


@login_required
@never_cache

def station_function(requests):
    stations = Station_data.objects.all()
    context = {
        'stations': stations,
        'page': "station"
    }
    return render(requests,'station_html/station.html', context)