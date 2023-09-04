from django.db import models
from foodmenu.models import Order
from foodmenu.order_context_processors import *
from accounts.models import *
from django.contrib.auth.models import User
from audioop import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from creditcards.models import CardNumberField,CardExpiryField,SecurityCodeField
from django.db.models.signals import post_save

# Create your models here.

class Checkout(models.Model):
    """Model definition for Checkout."""
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)
    phone=models.CharField(max_length=20,verbose_name=_("phone"))
    cardholder=models.CharField(max_length=20,verbose_name=_("Card Holder"))
    cardnumber=CardNumberField(verbose_name=_("Card Number"),max_length=16)
    expire=CardExpiryField(verbose_name=_("Exepire Date"))
    security=SecurityCodeField(verbose_name=_("CCV"))
    order_delivery_date= models.DateTimeField(verbose_name=_("Delivery Date"),blank=True, null=True)

    def __str__(self):
        return 'User: ' +  self.order.user.username + ' --> Order id: ' + str(self.id)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
    
    
    
    
    
    
    
class PageAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_address= models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,default = "None")
    phone = models.CharField(max_length=50,default = "None")
    not_if_any = models.CharField( max_length=50,default = "None")
    
    def __str__(self):
        return 'user : ' + str(self.user) + '  ===> ' + 'address : ' + str(self.address) + '  ===> ' +' phone: ' + str(self.phone)
    
    
    
class PayPalPayment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    card_number = models.CharField(max_length=16)
    expiration = models.CharField(max_length=10)
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    page_address= models.ForeignKey(PageAddress, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return 'name : ' + str(self.name) + '  ===> ' + 'email : ' + str(self.email) + '  ===> ' +' total : ' + str(self.total)
    
class PTTBankPayment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    account_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    page_address= models.ForeignKey(PageAddress, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return 'name : ' + str(self.name) + '  ===> ' + 'email : ' + str(self.email) + '  ===> ' +' total : ' + str(self.total)
    
    
    
    
class MasterCartPayment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    card_number = models.CharField(max_length=16)
    expiration = models.CharField(max_length=10)
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    page_address= models.ForeignKey(PageAddress, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return 'name : ' + str(self.name) + '  ===> ' + 'email : ' + str(self.email) + '  ===> ' +' total : ' + str(self.total)
    