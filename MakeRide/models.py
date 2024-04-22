from django.db import models
from Bike_Station.models import Bike_Station
from Home.models import CustomUser

class Ride(models.Model):
    station = models.ForeignKey(Bike_Station, on_delete=models.CASCADE)
    ride_id = models.AutoField(primary_key=True,null= False,unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    total_time = models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.ride_id