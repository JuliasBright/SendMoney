# Generated by Django 3.0.8 on 2020-08-10 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0002_auto_20200730_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_register',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 11, 0, 31, 47, 563006)),
        ),
    ]
