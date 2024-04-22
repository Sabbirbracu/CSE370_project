from django.shortcuts import render
from Home.models import CustomUser
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def viewprofile(request):
    # user = CustomUser.objects.all()
    user = request.user
    page="viewprofile"
    return render(request,'view_profile/view_profile.html',{'page':page,'user':user})


def editprofile(request):
    user =  request.user
    if request.method == "POST":
        # id = request.POST.get('id')
        name = request.POST.get('name')
        nid = request.POST.get('nid')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if request.POST.get('admin')=="Yes" and request.POST.get('rider')=="No":
            user_type = "Admin"
        else:
            user_type= "Rider"
        
        # user.id = id
        user.first_name = name
        user.nid = nid
        user.email = email
        user.address = address
        user.user_type = user_type
        user.save()
        messages.success(request,"Your Profile is Up to Date")
        return redirect("view_profile")

    page="editprofile"
    return render(request,'edit_profile/edit_profile.html',{'page':page,'user':user})