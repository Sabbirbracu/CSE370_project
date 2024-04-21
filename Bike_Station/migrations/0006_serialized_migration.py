from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Bike_Station', '0005_alter_bike_station_station_id'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE bike_station AUTO_INCREMENT = 1001;")
    ]
