# Generated by Django 3.1 on 2020-09-11 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0013_auto_20200909_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_register',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 11, 3, 10, 16, 619755)),
        ),
    ]
