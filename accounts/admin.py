from django.contrib import admin
from.models import Profile,Address ,Static_Address

# Register your models here.

# class Address_A(admin.StackedInline):
#     model = Address 
#     extra = 1

class Address_A(admin.TabularInline):
    model = Address 
    extra = 1
    
    
class Address_Admin(admin.ModelAdmin):
    inlines = [Address_A]
    

admin.site.register(Profile,Address_Admin)
admin.site.register(Address)
admin.site.register(Static_Address)
