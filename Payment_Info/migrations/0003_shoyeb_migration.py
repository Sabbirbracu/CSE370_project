from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Payment_Info', '0002_auto_20240419_2008'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE payment_info AUTO_INCREMENT = 3001;")
    ]
