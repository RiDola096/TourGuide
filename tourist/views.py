from multiprocessing import context
import profile
from django.shortcuts import redirect, render
from .models import Tourist, Booking
from .forms import BookingForm
from guide.models import Guide
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def single_tourist(request, tourist_id):
    profile = Tourist.objects.get(id=tourist_id)
    context = {
        'profile': profile,
    }

    return render(request, 'tourist/single-tourist.html', context)

@login_required(login_url='login')
def tourist_bookings(request):
    tourist = request.user.tourist
    bookings = Booking.objects.filter(tourist=tourist)
    guides = [booking.guide for booking in bookings]
    context = {
        'bookings': bookings,
        'guides': guides,
    }
    return render(request, 'tourist/tourist-bookings.html', context)

@login_required(login_url='login')
def book_guide(request, guide_id):
    tourist = request.user.tourist
    guide = Guide.objects.get(id=guide_id)
    booking_form = BookingForm()
    context = {
        'tourist': tourist,
        'guide': guide,
        'form': booking_form,
    }
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, request.FILES)
        if booking_form.is_valid():
            booking_form = booking_form.save(commit=False)
            if guide is not None:
                Booking.objects.create(
                    tourist=tourist,
                    guide=guide,
                    offer=booking_form.offer,
                    trip_duration=booking_form.trip_duration
                )
                return redirect('tourist-bookings')
    return render(request, 'tourist/book-guide.html', context)

@login_required(login_url='login')
def cancel_booking(request, booking_id):
    tourist = request.user.tourist
    booking = Booking.objects.get(id=booking_id)
    if booking.tourist == tourist:
        booking.status = 'Cancelled'
        booking.save()
        return redirect('tourist-bookings')
    return redirect('tourist-bookings')
