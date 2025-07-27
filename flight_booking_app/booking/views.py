from django.shortcuts import render
from django.http import HttpResponse 
from booking.forms import FlightForm
from booking.models import Flight

# Create your views here.
def index(request):
    form = FlightForm()
    return render(request, 'booking/index.html', {"form": form})

def login(request):
    return HttpResponse("Login page")

def my_flights(request):
    return HttpResponse("My flights page")

def faq(request):
    return render(request, 'booking/faq.html')

def results(request):
    form = FlightForm(request.GET or None)  # handles empty or filled GET data

    flights = None  # default: no flights yet

    if form.is_valid():
        departure = form.cleaned_data['departure_airport']
        arrival = form.cleaned_data['arrival_airport']
        departure_date = form.cleaned_data['departure_date']
        arrival_date = form.cleaned_data.get('arrival_date')

        # Build filters dynamically so optional fields don't break the search
        filters = {'departure_airport': departure, 'departure_date': departure_date}
        if arrival:  # only filter by arrival if filled
            filters['arrival_airport'] = arrival
        if arrival_date:  # only filter by arrival_date if filled
            filters['arrival_date'] = arrival_date

        flights = Flight.objects.filter(**filters)

    return render(request, 'booking/results.html', {'form': form, 'flights': flights})
