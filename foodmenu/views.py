from django.shortcuts import render
from accounts.models import *
from payment.models import PageAddress
from .models import BookATable,Restaurantmenu,Order,OrderDetails
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

from django.shortcuts import render ,redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden
# from.models import Checkout

# @login_required(login_url='/accounts/signin')
def add_to_cart(request):
    if request.user.is_authenticated:
        if 'product' in request.GET and 'product_price' in request.GET and 'qty' in request.GET:
            product= request.GET['product']
            qty= request.GET['qty']
            order= Order.objects.all().filter(user=request.user,is_finished=False)
            productname=Restaurantmenu.objects.get(slug=product)
            if order:
                old_order=Order.objects.get(user=request.user,is_finished=False)
                if OrderDetails.objects.all().filter(order=old_order,product=productname).exists():
                    order_detials=OrderDetails.objects.get(order=old_order,product=productname)
                    order_detials.quantity += int(qty)
                    order_detials.save()
                else:
                    order_detials=OrderDetails.objects.create(
                        product=productname,
                        order=old_order,
                        cost=productname.Price,
                        quantity=qty)
            else:
                new_order=Order()
                new_order.user=request.user
                new_order.order_date=timezone.now()
                new_order.is_finished=False
                new_order.save()
                order_detials=OrderDetails.objects.create(
                    product=productname,
                    order=new_order,
                    cost=productname.Price,
                    quantity=qty)
            messages.success(request,'Product added successfully To Cart')
            return redirect ('/restaurantMenu')
        else:
            messages.error(request,'Error To Add in Cart')
            return redirect ('restaurantMenu')
    else:
    
        messages.error(request,'You Must Be Login')
        return redirect ('/restaurantMenu')

from django.core.exceptions import ObjectDoesNotExist
def remove_from_Cart(request,orderdetials_id):
    try:
        orderdetials = OrderDetails.objects.get(id=orderdetials_id)
        if request.user.id == orderdetials.order.user.id:
            orderdetials.delete()
            return redirect('/restaurantMenu')
        else:
            return HttpResponseForbidden("You don't have permission to edit this cart.")
    except ObjectDoesNotExist:
        return HttpResponseNotFound("OrderDetails not  found.")


# Create your views here.
def Home(request):
    # You Are In Page Home
    context = {'name': 'Value from context'}
    return render(request,'food/home.html',context)

@login_required(login_url='/accounts/signin')
def booktable(request):
    # You Are In Page BookATable
    if request.method == 'POST' :
        ChooseTableSize = request.POST.get('table-size')
        ChooseADay = request.POST.get('booking-date')
        ChooseATime = request.POST.get('booking-time')
        ChooseAddressTable = request.POST.get('text-table')
        NotesIfAny = request.POST.get('text-notes')

        booking = BookATable.objects.create(
        ChooseTableSize=ChooseTableSize,
        ChooseADay=ChooseADay,
        ChooseATime=ChooseATime,
        ChooseAddressTable=ChooseAddressTable,
        NotesIfAny=NotesIfAny,)
        
        context = {'booking': booking}
        return render(request, 'food/bookatable.html',context)
    else:
        return render(request, 'food/bookatable.html')
    


@login_required(login_url='/accounts/signin')
def RestaurantMenu(request):
    # You Are In Page RestaurantMenu
    food_list = Restaurantmenu.objects.all()
    name = ""
    if 'search' in request.GET:
        food_list1 = Restaurantmenu.objects.all()
        name = request.GET['search']
        if name:
            food_list = food_list1.filter(Name__icontains=name)
    context = {'restaurantmenu': food_list}  
    return render(request, 'food/Restmenu.html',context)


@login_required(login_url='/accounts/signin')
def Reservation(request):
    # You Are In Page Reservation
    
    static_adress=Address.objects.filter(user=request.user.profile)
    existing_page_address = PageAddress.objects.filter(user=request.user, order_address__is_finished=False).last()

    if existing_page_address is not None:
        # User has already added an address for the order
        
        return redirect('/payment')
    address=None
    phone=None
    not_if_any=None
    if request.method=='POST':
        address=request.POST['address']
        phone=request.POST['phone']
        not_if_any=request.POST['not_if_any']
        order_address=Order.objects.filter(user=request.user).last()
        page_address=PageAddress(
                        user=request.user,
                        address=address,
                        phone=phone,
                        not_if_any=not_if_any,
                        order_address=order_address)
        page_address.save()
        return redirect('/payment')
    context={'static_adress':static_adress}
    return render(request,'food/reservation.html',context)










    
    # if request.method == 'POST':
    #     Name = request.POST.get('name')
    #     Address = request.POST.get('address')
    #     Phone = request.POST.get('phone')
    #     NotesIfAny = request.POST.get('text')
    #     fooddelivery = FoodDelivery.objects.create(Name=Name, Address=Address, Phone=Phone,NotesIfAny=NotesIfAny)
    #     context = {'fooddelivery': fooddelivery}
    #     return render(request,'food/reservation.html',context)
    # else:
    #     return render(request,'food/reservation.html')
    


# foreign key in Django 
# context_processors.py

