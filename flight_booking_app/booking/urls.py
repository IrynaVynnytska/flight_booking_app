from django.urls import path 
from booking import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('register.html', views.register, name='register'),
    path('my_flights/', views.my_flights, name='my_flights'),
    path('book/<int:flight_number>/', views.book_flight, name='book_flight'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('faq.html', views.faq, name='faq'),
    path('results.html', views.results, name='results'),
]