from django.db import models

class Rewards(models.Model):
    Rewards_id = models.AutoField(primary_key=True)
    Points = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = "rewards"
