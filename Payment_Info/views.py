from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from MakeRide.models import Ride
from .models import Payment_Info
from Rewards.models import Rewards
from django.contrib import messages
from django.db.models import Sum


@login_required
@never_cache
def payment(request):
    latest_ride = Ride.objects.latest('ride_id')
    total_time = latest_ride.total_time
    cost_per_min = 300
    total_amount = total_time * cost_per_min
    origin_amount = total_amount 
    user_total_points = request.user.rewards.aggregate(total_points=Sum('Points'))['total_points']
    
    if user_total_points is not None:
        if user_total_points >= 500:
            if total_amount >= 50:
                total_amount -= 50
    else:
        user_total_points = 0


    if request.method == "POST":
        ride_id = latest_ride.pk
        payment_info = Payment_Info.objects.create(cost_per_min=cost_per_min, total_amount=total_amount, ride_id=ride_id)
        payment_info.save()

        if user_total_points >= 500:
            if origin_amount >= 50:
                points = -500
            else:
                points = total_amount
        else:
            points = total_amount
        latest_payment = Payment_Info.objects.latest('payment_id')
        payment_id = latest_payment
            
        reward = Rewards(payment=payment_id, Points=points)
        reward.save()
        request.user.rewards.add(reward)
        
        # print("User Total Points", user_points)
        messages.success(request,"Your payment is Successfull.")
        return redirect("dashboard")

    page = "payment"
    return render(request, 'payment_html/payment.html', {'page': page, 'total_time': total_time, 'total_amount': total_amount})
