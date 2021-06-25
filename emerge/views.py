from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from admins.models import User

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print(username, '  ', password)
            login(request, user)
            print(username, '  ', password)
            roles = request.user.role
            if request.user.is_buser:
                return redirect('udashboard')
            elif request.user.is_manager:
                return redirect('mdashboard')
            else:
                return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            print(messages)
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')

def logout(request):
    logout(request)
    return redirect('/')
