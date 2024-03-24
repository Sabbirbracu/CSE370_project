from django.shortcuts import render

# Create your views here.
def index(requests):
    page = "index"
    return render(requests,'home_html/index.html',{'page':page})

def login(requests):
    page = "login"
    return render(requests,'home_html/login.html',{'page':page})

def base(requests):
    page="base"
    return render(requests,'home_html/base.html',{'page':page})


def register(requests):
    page = "register"
    return render(requests,'home_html/register.html',{'page':page})