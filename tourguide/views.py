from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from guide.models import Guide


@login_required(login_url='login')
def account(request):
    profile = request.user
    profile_type = 'Guide'
    try:
        profile = profile.guide
        profile_type = 'Guide'
    except:
        profile = profile.tourist
        profile_type = 'Guide'

    context = {
        'profile': profile,
        'profile_type': profile_type,
    }
    
    return render(request, 'account.html', context)

@login_required(login_url='login')
def bookings(request):
    profile = request.user
    try:
        profile = profile.guide
        print('u')
        return redirect('guide-bookings')
    except:
        return redirect('tourist-bookings')
