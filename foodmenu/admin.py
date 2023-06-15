from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BookATable)
admin.site.register(Restaurantmenu)
admin.site.register(FoodDelivery)
admin.site.register(Order)
admin.site.register(OrderDetails)