from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from accounts.forms import AuthenticationForm, RegistrationForm

def login(request):
    ''' Log in view'''

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST, password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
        template = 'accounts/login.html'
        context = {
            'form': form
        }
    return render(request, template, context)

def register(request):
    ''' User Registration View'''

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid:
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        template = 'accounts/register.html'
        context = {
            'form': form
        }
    return render(request, template, context)

def logout(request):
    ''' Log out View'''
    django_logout(request)
    return redirect('/')
