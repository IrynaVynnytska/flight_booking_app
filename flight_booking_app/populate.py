import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'flight_booking_app.settings')
from datetime import date, time
import django
django.setup()

from booking.models import Airline, Flight, Booking, Passenger
from django.contrib.auth.models import User

def populate():
    airline1, _ = Airline.objects.get_or_create(name="British Airways", code="BA")
    airline2, _ = Airline.objects.get_or_create(name="Lufthansa", code="LH")
    airline3, _ = Airline.objects.get_or_create(name="Delta Airlines", code="DL")

    flight1, _ = Flight.objects.get_or_create(
        airline=airline1,
        flight_number="BA101",
        departure_airport="London Heathrow",
        arrival_airport="New York JFK",
        departure_date=date(2025, 7, 30),
        departure_time=time(9, 0),
        arrival_date=date(2025, 7, 30),
        arrival_time=time(12, 0),
        price=450.00
    )

    flight2, _ = Flight.objects.get_or_create(
        airline=airline2,
        flight_number="LH220",
        departure_airport="Frankfurt",
        arrival_airport="Paris CDG",
        departure_date=date(2025, 8, 1),
        departure_time=time(14, 30),
        arrival_date=date(2025, 8, 1),
        arrival_time=time(15, 45),
        price=120.00
    )

    flight3, _ = Flight.objects.get_or_create(
        airline=airline3,
        flight_number="DL305",
        departure_airport="Atlanta",
        arrival_airport="Los Angeles",
        departure_date=date(2025, 8, 5),
        departure_time=time(7, 15),
        arrival_date=date(2025, 8, 5),
        arrival_time=time(9, 30),
        price=300.00
    )

    user1, created1 = User.objects.get_or_create(username="alice")
    if created1:
        user1.set_password("password123")
        user1.save()

    user2, created2 = User.objects.get_or_create(username="bob")
    if created2:
        user2.set_password("password123")
        user2.save()

    # --- PASSENGERS ---
    passenger1, _ = Passenger.objects.get_or_create(user=user1, phone_number="123456789", passport_number="P123456")
    passenger2, _ = Passenger.objects.get_or_create(user=user2, phone_number="987654321", passport_number="P654321")

    # --- BOOKINGS ---
    Booking.objects.get_or_create(passenger=user1, flight=flight1, num_tickets=1, status='CONFIRMED')
    Booking.objects.get_or_create(passenger=user1, flight=flight2, num_tickets=2, status='CONFIRMED')
    Booking.objects.get_or_create(passenger=user2, flight=flight3, num_tickets=1, status='CANCELLED')


    print(" Database populated with sample airlines, flights, passengers and bookings!")


if __name__ == '__main__':
    populate()


