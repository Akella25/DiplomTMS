from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_authorization.forms import CreateNewUserForm

def registration(request):


    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNewUserForm()

    return render(request, 'registr.html', {'form': form})



