from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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
        print(request.POST)
        print("user Type:",request.POST.get('user_type'))
        form = CustomUserCreationForm(request.POST)
        print([i for i in form.errors])
        print(form.errors)
        if form.is_valid():
            print("ok")
            form.save()
            return redirect('/')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    page = "register"
    return render(request, 'home_html/register.html', {'page': page})