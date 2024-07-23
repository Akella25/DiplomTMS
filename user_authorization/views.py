from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_authorization.forms import CreateNewUserForm, LoginAuthenticationForm, BookRoomForm
from django.contrib.auth import login, logout
from hotel.models import Booking, Hotel, Room


def registration(request):
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'])
            login(request, user)

            return redirect('home')
    else:
        form = CreateNewUserForm()

    return render(request, 'registr.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginAuthenticationForm(request.POST)
        user = User.objects.filter(username=form.request['username']).first()
        if user.check_password(form.request['password']):
            login(request, user)
            return redirect('home')
    else:
        form = LoginAuthenticationForm()

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')


def info_user(request):
    user_id = request.user.id
    bookings = Booking.objects.prefetch_related('room_pay').filter(client=user_id).all()

    hotels = []
    for booking in bookings:
        hotel_id = booking.room_pay.hotel

        hotels.append([booking, hotel_id])



    return render(request, 'info_user.html', {'hotels': hotels})


def book_room_form(request, pk):
    form = BookRoomForm()
    form.fields['room_pay'].queryset = Room.objects.filter(hotel=pk)

    return render(request, 'booking.html', {'form': form})


def book_room(request):
    form = BookRoomForm(request.POST)
    if form.is_valid():
        check_in_date = form.cleaned_data['check_in_date']
        eviction_date = form.cleaned_data['eviction_date']
        room_pay = form.cleaned_data['room_pay']

        booking = Booking.objects.create(client=request.user, check_in_date=check_in_date, eviction_date=eviction_date,
                                         room_pay=room_pay)

        return redirect('info_user')

    return render(request, 'booking.html', {'form': form})



def del_booking(request, pk):
    booking = Booking.objects.get(id=pk).delete()

    return redirect('info_user')
