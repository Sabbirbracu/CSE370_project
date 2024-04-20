from django.shortcuts import render

# Create your views here.

def ride(request):
    page = "ride"
    return render(request,'ride/ride.html')