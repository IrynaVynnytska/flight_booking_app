from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import timedelta
from booking.forms import FlightForm, PassengerProfileForm, PassengerForm
from booking.models import Flight


def index(request):
    form = FlightForm()
    return render(request, 'booking/index.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('booking:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'booking/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('booking:index'))


def register(request):
    registered = False

    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)
        profile_form = PassengerProfileForm(request.POST)

        if passenger_form.is_valid() and profile_form.is_valid():

            passenger = passenger_form.save()
            passenger.set_password(passenger.password)
            passenger.save()

            profile = profile_form.save(commit=False)
            profile.passenger = passenger

        else :
            print(passenger_form.errors, profile_form.errors)
    else:
        passenger_form = PassengerForm()
        profile_form = PassengerProfileForm()

    return render(request,
                'booking/register.html',
                context = {'passenger_form': passenger_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def my_flights(request):
    return HttpResponse("You are logged in.")


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

        note = None
        if not flights.exists():
            flights = Flight.objects.filter(
                departure_airport=departure,
                arrival_airport=arrival,
                departure_date__range=[departure_date, departure_date + timedelta(days=5)]
            )
            if flights.exists():
                note = "No flights on your exact date. Showing flights up to 5 days later."


    return render(request, 'booking/results.html', {'form': form, 'flights': flights, 'note': note})
