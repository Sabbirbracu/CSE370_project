from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser

def index(requests):
    page = "index"
    return render(requests,'home_html/index.html',{'page':page})

def login_view(requests):
    if requests.method == 'POST':
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        user = authenticate(requests, email=email, password=password)

        if user is not None:
            login(requests, user)
            # u_mail = CustomUser.objects.raw("SELECT username, first_name FROM Home_customuser")
            # print(u_mail)
            if user.user_type == "Admin":
                return redirect("admin_dashboard")
            else:
                return redirect('dashboard')
        
        else:
            # Invalid credentials, show an error message
            messages.error(requests, 'Invalid email or password.')
    page = "login"
    return render(requests, 'home_html/login.html', {'page': page})

def view_profile(request):
    return render(request, 'view_profile/view_profile.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You are looged out")
    return redirect('login') 


def base(requests):
    page="base"
    return render(requests,'home_html/base.html',{'page':page})


CustomUser = get_user_model()
def register(request):
    if request.method == 'POST':

        # Checking wheter NID is valid or Not
        nid = request.POST.get('nid')
        for i in nid:
            if 48 <= ord(i) <= 57:
                pass
            else:
                messages.error(request,"Opps! You have entered invalid NID")
                return redirect('register')
                
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():

            form.save()
            messages.success(request,"You have succefully registerd")
            return redirect('login')  # Redirect to login page after successful registration
        
        else:
            # Handle the case when the form is invalid
            # errors = form.errors.get('email', None)
            # if errors:
            #     print(errors,"this is errors and i added it to see the error list")

            #     for i in errors:
            #         messages.error(request,f'{i}')
            #         print(i)
                # messages.error(request, f'Opps! {[i for i in errors]}')
            
            # Another technique
            for field, errors in form.errors.items():
                for error in errors:
                    print(error)
                    messages.error(request, f'{field.capitalize()}: {error}')
                    return redirect('register')  # Redirect back to registration page with error messages         
    else:
        form = CustomUserCreationForm()
    page = "register"
    return render(request, 'home_html/register.html', {'page': page})

