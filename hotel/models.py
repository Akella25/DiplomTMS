from django.contrib.auth.models import User
from django.db import models


class Citi(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.SmallIntegerField(default=1)
    rooms = models.IntegerField()
    address = models.CharField(max_length=200)
    swimming_pool = models.BooleanField(default=False)
    city = models.ForeignKey('Citi', on_delete=models.CASCADE, related_name='hotel')
    picturess = models.ImageField(upload_to='books/%Y-%m-%d/', null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    room_price = models.IntegerField()
    room_type = models.CharField(max_length=50, null=True, blank=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='room')

    def __str__(self):
        return str(self.number)

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateField()
    eviction_date = models.DateField()
    room_pay = models.OneToOneField('Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.client.username
