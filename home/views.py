from django.shortcuts import render
from hotel.models import Hotel
import random


def home(request):
    hotels = Hotel.objects.all().order_by('-stars')
    hotel = random.choice(list(hotels))

    return render(request, 'home.html', {'hotel': hotel})




