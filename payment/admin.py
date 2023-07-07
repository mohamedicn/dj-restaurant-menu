from django.contrib import admin
from .models import Checkout ,PayPalPayment,PTTBankPayment ,PageAddress,MasterCartPayment
# Register your models here.
# from foodmenu.models import OrderDetails

# class Address_A(admin.TabularInline):
#     model = OrderDetails 
#     extra = 1
    
    
# class Address_Admin(admin.ModelAdmin):
#     inlines = [Address_A]
    
admin.site.register(Checkout)
admin.site.register(PayPalPayment)
admin.site.register(PTTBankPayment)
admin.site.register(PageAddress)
admin.site.register(MasterCartPayment)

