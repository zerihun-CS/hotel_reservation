from django.shortcuts import render
from .models import Reservation
# Create your views here.


def index(request):
    reservation = Reservation.objects.all()

    return render(request,'view_booking.html',{'reservation':reservation})