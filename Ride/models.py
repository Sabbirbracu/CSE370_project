from django.db import models

class Ride(models.Model):
    ride_id = models.CharField(primary_key= True, null= False, unique=True, max_length=15)
    start_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    total_time = models.IntegerField()
    
    
    class Meta:
        managed = True
        db_table = 'ride'