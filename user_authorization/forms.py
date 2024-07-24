from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from hotel.models import Booking, Room


class CreateNewUserForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginAuthenticationForm(AuthenticationForm):
    class Meta(CreateNewUserForm.Meta):
        model = User
        fields = ('username', 'password')


class BookRoomForm(forms.ModelForm):

    room_pay = forms.ModelChoiceField(queryset=Room.objects.all(), label='Номер комнаты')
    check_in_date = forms.DateField(label='Дата заселения')
    eviction_date = forms.DateField(label='Дата выселения')

    class Meta:
        model = Booking
        fields = ('check_in_date', 'eviction_date', 'room_pay')
