from django.contrib import admin
from .models import *

# Register your models here.

class Property_Detail(admin.TabularInline):
    model = OrderDetails 
    extra = 1
    
class OrderAdmin(admin.ModelAdmin):
    inlines=[Property_Detail]
    
admin.site.register(BookATable)
admin.site.register(Restaurantmenu)
# admin.site.register(FoodDelivery)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetails)