# Generated by Django 5.0.4 on 2024-04-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('Station_ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Station_Name', models.CharField(max_length=20)),
                ('Number_of_Bikes', models.IntegerField()),
                ('Station_Status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'station',
                'managed': False,
            },
        ),
    ]
