from django.shortcuts import render

# Create your views here.
def base(requests):
    return render(requests,'home_html/base.html')


def index(requests):
    return render(requests,'home_html/index.html')
