from django.urls import path 
from booking import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('my_flights.html', views.my_flights, name='my_flights'),
    path('faq.html', views.faq, name='faq'),
    path('results.html', views.results, name='results'),
]