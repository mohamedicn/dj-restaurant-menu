from django.db import models
from foodmenu.models import Order
from django.contrib.auth.models import User
from audioop import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from creditcards.models import CardNumberField,CardExpiryField,SecurityCodeField
# Create your models here.

class Payment(models.Model):
    pass



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
    