from django.contrib import admin
from booking.models import Airline, Flight, Passenger, Booking, Seats

# Register your models here.
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Seats)