from django.urls import path
from booking.views import booking_add_view

urlpatterns = [
    path('add/', booking_add_view, name='add_booking'),
]
