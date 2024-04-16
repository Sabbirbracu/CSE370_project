from django.db import models

class Station_data(models.Model):
    Station_ID = models.CharField(primary_key= True, null= False, max_length=15)
    Station_Name = models.CharField(max_length=20)
    Number_of_Bikes = models.IntegerField()
    Station_Status = models.CharField(max_length=15)
    

