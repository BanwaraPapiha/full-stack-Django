from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def main(request):
    context = {
        'flights': Flights.objects.all()
    }
    return render(request, 'list.html', context)

def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passengers.objects.exclude(flight=flight_id).all(),
    }
    return render(request, 'flight.html', context)

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flights.objects.get(pk=flight_id)
        passenger = Passengers.objects.get(pk=int(request.POST['info']))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))