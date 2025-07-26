from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return render(request, 'booking/index.html')

def login(request):
    return HttpResponse("Login page")

def my_flights(request):
    return HttpResponse("My flights page")

def faq(request):
    return render(request, 'booking/faq.html')
