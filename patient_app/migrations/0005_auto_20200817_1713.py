# Generated by Django 3.1 on 2020-08-17 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0004_auto_20200817_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_patient',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 17, 13, 22, 948620)),
        ),
        migrations.AlterField(
            model_name='patient_register',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 17, 13, 22, 947594)),
        ),
        migrations.AlterField(
            model_name='patient_register',
            name='image',
            field=models.ImageField(default='', upload_to='patient_app/images'),
        ),
    ]
