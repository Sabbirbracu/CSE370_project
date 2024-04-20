from django.db import models

class Payment_Info(models.Model):
    payment_id = models.AutoField(primary_key=True)  # ALTER TABLE payment AUTO_INCREMENT = 3001
    cost_per_min = models.IntegerField(default=5)
    date = models.DateField(auto_now_add=True)
    total_amount = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = 'payment_info'