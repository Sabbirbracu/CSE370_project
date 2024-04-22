from django.db import models
from Payment_Info.models import Payment_Info
from Home.models import CustomUser

class Rewards(models.Model):

    Rewards_id = models.AutoField(primary_key=True)
    Points = models.IntegerField(null=True)
    payment = models.OneToOneField(Payment_Info,on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser, related_name='rewards') 
    
    class Meta:
        managed = True
        db_table = "rewards"
