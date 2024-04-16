from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@login_required
@never_cache

def dashboard(requests):
    page = "dashboard"
    return render(requests,'Dashboard/dashboard.html',{'page':page})