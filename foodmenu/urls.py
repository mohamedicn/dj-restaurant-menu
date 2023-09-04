from django.urls import path
from . import views
from .api_view import *
app_name='foodmenu'



urlpatterns= [
    path('',views.Home, name = 'home'),
    path('booktable',views.booktable, name = 'booktable'),
    path('reservation',views.Reservation, name = 'reservation'),
    path('restaurantMenu',views.RestaurantMenu, name = 'restaurantMenu'),
    path('add_to_cart',views.add_to_cart, name = 'add_to_cart'),
    path('remove_from_Cart/<int:orderdetials_id>',views.remove_from_Cart, name = 'remove_from_Cart'),
    # path('search/', search, name='search'),


    # api
    path('api/food/list',FoodAPiList.as_view(),name='FoodAPiList'),
    path('api/food/list/<int:pk>',FoodAPiDetail.as_view(),name='FoodAPiDetail'),
    
    path('api/order/list',OrderAPiList.as_view(),name='OrderAPiList'),
    path('api/order/list/<int:order_id>/detail/', OrderDetailsByOrderIdAPIView.as_view(), name='order-detail'),
    
    path('api/add_to_cart/<int:order_id>/',AddToCartAPIView.as_view(), name = 'api_add_to_cart'),
]











