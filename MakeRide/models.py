from django.db import models

class Ride(models.Model):
    ride_id = models.AutoField(primary_key=True,null= False,unique=True)
    station = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    total_time = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.ride_id