from django.db import models

class Bike_Station(models.Model):
    Station_ID = models.AutoField(primary_key= True, null= False, unique=True)
    Station_Name = models.CharField(max_length=20)
    Number_of_Bikes = models.IntegerField()
    Station_Status = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'bike_station'