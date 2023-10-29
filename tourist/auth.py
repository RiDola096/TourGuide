from cmath import log
from django.shortcuts import render, redirect
from .forms import TouristForm
from django.contrib.auth import login


def tourist_signup(request):
    if request.user.is_authenticated:
        return redirect('guides')
    signup_form = TouristForm()
    context = {
        'form': signup_form,
        'submit_button_text': 'Sign Up',
    }

    if request.method == 'POST':
        signup_form = TouristForm(request.POST, request.FILES)
        if signup_form.is_valid():
            tourist = signup_form.save()
            login(request, tourist.user)
            return redirect('guides')
    
    return render(request, 'signup.html', context)
