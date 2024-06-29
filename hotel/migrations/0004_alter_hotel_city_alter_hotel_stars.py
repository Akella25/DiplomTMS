# Generated by Django 5.0.6 on 2024-06-27 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_booking_name_booking_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotel.citi'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.SmallIntegerField(default=1),
        ),
    ]