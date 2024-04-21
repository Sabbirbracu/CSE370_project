from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from MakeRide.models import Ride
from .models import Payment_Info

@login_required
@never_cache

def payment(request):
    latest_ride = Ride.objects.latest('ride_id')
    total_time = latest_ride.total_time
    cost_per_min = 5
    total_amount = total_time * cost_per_min

    if request.method == "POST":
        payment_info = Payment_Info.objects.create(cost_per_min=cost_per_min, total_amount=total_amount)
        payment_info.save()
        page = "dashboard"
        return render(request, 'Dashboard/dashboard.html', {'page': page})

    page = "payment"
    return render(request, 'payment_html/payment.html', {'page': page, 'total_time': total_time,'total_amount':total_amount})