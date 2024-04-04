from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def index(requests):
    page = "index"
    return render(requests,'home_html/index.html',{'page':page})



def login_view(requests):
    if requests.method == 'POST':
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        
        user = authenticate(requests, email=email, password=password)
        # print(user)
        if user is not None:
            login(requests, user)
            # Redirect to the dashboard or any other desired page
            return redirect('dashboard')
        else:
            # Invalid credentials, show an error message
            messages.error(requests, 'Invalid email or password.')
    page = "login"
    return render(requests, 'home_html/login.html', {'page': page})


def base(requests):
    page="base"
    return render(requests,'home_html/base.html',{'page':page})


CustomUser = get_user_model()
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # email = form.cleaned_data['email']
            # # Check if the email already exists
            print(messages)
            # if CustomUser.objects.filter(email=email).exists():
            #     messages.error(request, 'This email is already registered.Try another email or LogIn')
                
            #     return redirect('register')
            # else:
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
            
            # Another tech
            for field, errors in form.errors.items():
                for error in errors:
                    print(error)
                    messages.error(request, f'{field.capitalize()}: {error}')
                    return redirect('register')  # Redirect back to registration page with error messages
            else:
                messages.error(request, "An error occurred. Please try again.")



            # Capture and display all errors
            # for field, errors in form.errors.items():
            #     if isinstance(errors, dict):
            #         for subfield, suberrors in errors.items():
            #             for suberror in suberrors:
            #                 messages.error(request, f'{subfield.capitalize()}: {suberror}')
            #     else:
            #         for error in errors:
            #             messages.error(request, f'{field.capitalize()}: {error}')
            # return redirect('register')  
                
    else:
        form = CustomUserCreationForm()
    page = "register"
    return render(request, 'home_html/register.html', {'page': page})