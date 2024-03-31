from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def index(requests):
    page = "index"
    return render(requests,'home_html/index.html',{'page':page})



def login_view(requests):
    page = "login"
    return render(requests, 'home_html/login.html', {'page': page})



def base(requests):
    page="base"
    return render(requests,'home_html/base.html',{'page':page})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You have succefully registerd")
            return redirect('login')  # Redirect to login page after successful registration
        
    else:
        form = CustomUserCreationForm()
    page = "register"
    return render(request, 'home_html/register.html', {'page': page})