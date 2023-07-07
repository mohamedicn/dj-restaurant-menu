from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render ,redirect
# form .models import PayPalPayment ,PTTBankPayment
from foodmenu.models import Restaurantmenu ,Order
from .models import * 




# # Create your views here.
def Payment(request):
    name=None
    email=None
    card_number=None
    expiration=None
    cvv=None
    total=None
    if request.method=='POST' and 'paypal_button' in request.POST :
        name=request.POST['name']
        email=request.POST['email']
        card_number=request.POST['card_number']
        expiration=request.POST['expiration']
        cvv=request.POST['cvv']
        total=request.POST['total']
        if Order.objects.all().filter(user=request.user,is_finished=False):
            order=Order.objects.get(user=request.user,is_finished=False)
            page_address=PageAddress.objects.filter(user=request.user).last()
            paypal_payment=PayPalPayment(
                            name=name,
                            email=email,
                            card_number=card_number,
                            expiration=expiration,
                            cvv=cvv,
                            total=total,
                            page_address=page_address,)
            paypal_payment.save()
            order.is_finished=True
            order.save()
        return redirect('/')
    # ------------------------------

    name_bank=None
    email_bank=None
    account_number=None
    amount=None
    total_bank=None
    if request.method == 'POST' and 'pttPayment_button' in request.POST:
        name_bank = request.POST['name_bank']
        email_bank = request.POST['email_bank']
        account_number = request.POST['account_number']
        amount = request.POST['amount']
        total_bank = request.POST['total_bank']
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            page_address=PageAddress.objects.filter(user=request.user).last()
            pttPayment=PTTBankPayment(
                name=name_bank,
                email=email_bank,
                account_number=account_number,
                amount=amount,
                total=total_bank,
                page_address=page_address,)
            pttPayment.save()
            order.is_finished = True
            order.save()
        return redirect('/')
    
    # ------------------------------

    name_mcard=None
    email_mcard=None
    card_number_mcard=None
    expiration_mcard=None
    total_mcard=None
    cvv_mcard=None
    if request.method == 'POST' and 'mcard_Payment_button' in request.POST:
        name_mcard = request.POST['name_mcard']
        email_mcard = request.POST['email_mcard']
        card_number_mcard = request.POST['card_number_mcard']
        expiration_mcard = request.POST['expiration_mcard']
        total_mcard = request.POST['total_mcard']
        cvv_mcard = request.POST['cvv_mcard']
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            page_address=PageAddress.objects.filter(user=request.user).last()
            pttPayment=MasterCartPayment(
                name=name_mcard,
                email=email_mcard,
                card_number=card_number_mcard,
                expiration=expiration_mcard,
                total=total_mcard,
                cvv=cvv_mcard,
                page_address=page_address,)
            pttPayment.save()
            order.is_finished = True
            order.save()
        return redirect('/')

    return render(request,'payment/payment.html')