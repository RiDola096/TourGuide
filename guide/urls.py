from django.urls import path, include
from . import views, auth


urlpatterns = [
    path('signup/', auth.guide_signup, name='guide-signup'),
    path('edit/', auth.guide_edit, name='guide-edit'),
    path('guides/', views.guides_list, name='guides'),
    path('single-guide/<str:guide_id>/', views.single_guide, name='single-guide'),
    path('bookings/', views.guide_bookings, name='guide-bookings'),
    path('accept-booking/<str:booking_id>/', views.accept_booking, name='guide-accept-booking'),
    path('cancel-booking/<str:booking_id>/', views.cancel_booking, name='guide-cancel-booking'),
]