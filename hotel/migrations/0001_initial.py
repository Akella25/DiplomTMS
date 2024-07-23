# Generated by Django 5.0.6 on 2024-07-16 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Citi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stars', models.SmallIntegerField(default=1)),
                ('rooms', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('picturess', models.ImageField(blank=True, null=True, upload_to='books/%Y-%m-%d/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotel.citi')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('room_price', models.IntegerField()),
                ('room_type', models.CharField(blank=True, max_length=50, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateField()),
                ('eviction_date', models.DateField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_pay', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
    ]
