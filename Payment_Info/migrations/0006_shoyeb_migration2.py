from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Payment_Info', '0005_auto_20240420_1205'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE payment AUTO_INCREMENT = 3001;")
    ]
