from django import forms
from django.contrib.auth.models import User
from booking.models import Flight, Passenger


class FlightForm(forms.Form):
    departure_airport = forms.ChoiceField()
    arrival_airport = forms.ChoiceField(required=False)
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        departure_airports = Flight.objects.values_list('departure_airport', flat=True).distinct()
        arrival_airports = Flight.objects.values_list('arrival_airport', flat=True).distinct()

        departure_choices = [('', 'Select a Departure Airport')] + [(a, a) for a in departure_airports]
        arrival_choices = [('', 'Select an Arrival Airport')] + [(a, a) for a in arrival_airports]

        self.fields['departure_airport'].choices = departure_choices
        self.fields['arrival_airport'].choices = arrival_choices

class PassengerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PassengerProfileForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('phone_number', 'passport_number',)

