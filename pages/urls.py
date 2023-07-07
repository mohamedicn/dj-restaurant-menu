from django.urls import path
from . import views

urlpatterns= [
path('',views.Home, name = 'home'),
path('bookatable',views.BookATable, name = 'bookatable'),
path('reservation',views.Reservation, name = 'reservation'),
path('aboutus',views.AboutUs, name = 'aboutus'),
path('contact',views.Contact, name = 'contact'),
]







