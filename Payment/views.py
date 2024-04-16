from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@login_required
@never_cache

def payment(requests):
    page = "payment"
    return render(requests,'payment_html/payment.html', {'page':page})