from django import forms
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('table')
            else:
                return redirect('home')
    
    context = {'form': form}
    return render(request, 'login.html', context)