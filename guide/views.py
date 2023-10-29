from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Guide
from tourist.models import Booking


@login_required(login_url='login')
def guides_list(request):
    try:
        request.user.guide
        return redirect('account')
    except:
        pass
    guides_list = Guide.objects.all()

    if request.method == 'POST':
        location_hint = request.POST['location'].lower()
        guides_list = Guide.objects.filter(location__contains=location_hint)

    context = {
        'guides_list': guides_list,
    }
    return render(request, 'guide/guides.html', context)

def single_guide(request, guide_id):
    profile = Guide.objects.get(id=guide_id)
    context = {
        'profile': profile,
    }
    return render(request, 'guide/single-guide.html', context)

@login_required(login_url='login')
def guide_bookings(request):
    guide = request.user.guide
    bookings = Booking.objects.filter(guide=guide)

    context = {
        'profile': guide,
        'bookings': bookings,
    }

    return render(request, 'guide/guide-bookings.html', context)

@login_required(login_url='login')
def accept_booking(request, booking_id):
    guide = request.user.guide
    booking = Booking.objects.get(id=booking_id)
    if booking.guide == guide:
        booking.status = 'Accepted'
        booking.save()
        return redirect('guide-bookings')
    return redirect('guide-bookings')

@login_required(login_url='login')
def cancel_booking(request, booking_id):
    guide = request.user.guide
    booking = Booking.objects.get(id=booking_id)
    if booking.guide == guide:
        booking.status = 'Cancelled'
        booking.save()
        return redirect('guide-bookings')
    return redirect('guide-bookings')
