from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from MakeRide.models import Ride
from .models import Payment_Info
from Rewards.models import Rewards

@login_required
@never_cache

def payment(request):
    latest_ride = Ride.objects.latest('ride_id')
    total_time = latest_ride.total_time
    cost_per_min = 5
    total_amount = total_time * cost_per_min
    get_id = latest_ride.pk

    if request.method == "POST":
        ride_id = Ride.objects.get(ride_id=get_id)
        payment_info = Payment_Info.objects.create(cost_per_min=cost_per_min, total_amount=total_amount,ride=ride_id)
        payment_info.save()


        points = total_amount
        latest_payment = Payment_Info.objects.latest('payment_id')
        get_payment_id = latest_payment.pk
        payment_id = Payment_Info.objects.get(payment_id=get_payment_id)
        reward = Rewards(payment=payment_id,Points=points)
        reward.save()
        page = "dashboard"
        return render(request, 'Dashboard/dashboard.html', {'page': page})

    page = "payment"
    return render(request, 'payment_html/payment.html', {'page': page, 'total_time': total_time,'total_amount':total_amount})