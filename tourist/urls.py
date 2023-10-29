from django.urls import path, include
from . import views, auth


urlpatterns = [
    path('signup/', auth.tourist_signup, name='tourist-signup'),
    path('single-tourist/<str:tourist_id>/', views.single_tourist, name='single-tourist'),
    path('tourist-bookings/', views.tourist_bookings, name='tourist-bookings'),
    path('book-guide/<str:guide_id>', views.book_guide, name='book-guide'),
    path('cancel-booking/<str:booking_id>/', views.cancel_booking, name='tourist-cancel-booking'),
]