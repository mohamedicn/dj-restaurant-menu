from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from foodmenu.models import Restaurantmenu 
from .models import * 



# # Create your views here.


def Payment(request):
    # Yor Are In Page Payment
    context = { 'name': 'Payment'}
    return render(request, 'payment/payment.html', context)
    
