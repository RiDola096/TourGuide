from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_user(request):
    if request.user.is_authenticated:
        return redirect('account')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user is None:
                return redirect('login')
        finally:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('guides')
