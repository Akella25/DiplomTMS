from django.shortcuts import render
from hotel.models import Hotel


def home(request):
    hotels = Hotel.objects.all().order_by('-stars')

    return render(request, 'home.html', {'hotels': hotels})

