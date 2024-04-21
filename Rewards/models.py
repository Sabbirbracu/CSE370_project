from django.db import models
from Payment_Info.models import Payment_Info

class Rewards(models.Model):

    Rewards_id = models.AutoField(primary_key=True)
    Points = models.IntegerField(null=True)
    payment = models.OneToOneField(Payment_Info,on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = "rewards"
