
from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    page = "admin_dashboard"
    return render(request,"admin_home/admin_dashboard.html",{'page':page})

def update_station(request):
    page = "update_station"
    return render(request,"admin_home/update_station.html",{'page':page})