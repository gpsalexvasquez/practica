from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login 
from django.contrib import messages

def public_home(request):
    return render(request, 'home.html')

@login_required
def home_admin(request):
    return render(request, 'home_admin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username = username,
            password = password,
        )
        if user is not None:
            auth_login(request, user)
            return redirect('home_admin')
        else:
            messages.error(request,"Usuario o contraseña Incorrecta")
            return redirect('login')
        
    return render (request, 'registration/login.html')

def salir (request):
    logout(request)
    return redirect ('home')