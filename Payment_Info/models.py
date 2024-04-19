from django.db import models

class Payment_Info(models.Model):
    payment_id = models.AutoField(primary_key=True)  # ALTER TABLE payment AUTO_INCREMENT = 3001
    total_time = models.IntegerField()
    total_amount = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = 'payment_info'