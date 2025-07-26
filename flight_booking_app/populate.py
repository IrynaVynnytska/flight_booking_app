import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'flight_booking_app.settings')
from datetime import date, time
import django
django.setup()
from booking.models import Airline, Flight

def populate():
    airline1, _ = Airline.objects.get_or_create(name="British Airways", code="BA")
    airline2, _ = Airline.objects.get_or_create(name="Lufthansa", code="LH")
    airline3, _ = Airline.objects.get_or_create(name="Delta Airlines", code="DL")

    Flight.objects.get_or_create(
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

    Flight.objects.get_or_create(
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

    Flight.objects.get_or_create(
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

    print("✅ Database populated with sample airlines and flights!")


if __name__ == '__main__':
    populate()