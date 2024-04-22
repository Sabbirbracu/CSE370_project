from django.shortcuts import render,HttpResponse
from . models import Rewards,Payment_Info

# Create your views here
def rewards(request):
    rewards = Rewards.objects.all()
    context = {
        'rewards': rewards,
        'page': "rewards"
        
    }
    return render(request,'rewards/rewards.html', context)
