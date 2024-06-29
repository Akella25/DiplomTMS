from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_authorization.forms import CreateNewUserForm, LoginAuthenticationForm
from django.contrib.auth import login, logout


def registration(request):
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            form.save()
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