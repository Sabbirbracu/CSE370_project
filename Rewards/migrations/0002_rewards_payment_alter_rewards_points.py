# Generated by Django 5.0.3 on 2024-04-21 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment_Info', '0005_payment_info_ride'),
        ('Rewards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rewards',
            name='payment',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, to='Payment_Info.payment_info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rewards',
            name='Points',
            field=models.IntegerField(null=True),
        ),
    ]
