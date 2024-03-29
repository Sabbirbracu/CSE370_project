from django.shortcuts import render

# Create your views here.
def dashboard(requests):
    page = "dashboard"
    return render(requests,'Dashboard/dashboard.html',{'page':page})