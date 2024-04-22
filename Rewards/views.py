from django.shortcuts import render,HttpResponse
from . models import Rewards,Payment_Info
from django.db.models import Sum

# Create your views here
def rewards(request):
    user_points = request.user.rewards.aggregate(total_points=Sum('Points'))['total_points']
    context = {
        'user_points': user_points,
        'page': "rewards"
        
    }
    return render(request,'rewards/rewards.html', context)
