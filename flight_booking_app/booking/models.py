from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Airline(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number}: {self.departure_airport} → {self.arrival_airport}"
    

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    passport_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
    

class Booking(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled')
    ], default='CONFIRMED')

    def __str__(self):
        return f"Booking {self.id} - {self.passenger.username} for {self.flight.flight_number}"


class Seats(models.Model):
    pass