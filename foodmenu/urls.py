from django.urls import path
from . import views
app_name='foodmenu'

urlpatterns= [
path('',views.Home, name = 'home'),
path('booktable',views.booktable, name = 'booktable'),
path('reservation',views.Reservation, name = 'reservation'),
path('restaurantMenu',views.RestaurantMenu, name = 'restaurantMenu'),
path('add_to_cart',views.add_to_cart, name = 'add_to_cart'),
# path('search/', search, name='search'),
]











