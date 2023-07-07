from.models import *

def order_payment(request):
    if  request.user.is_authenticated:
        if Order.objects.filter(user=request.user, is_finished=False).exists():
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.filter(order=order)
            total=0
            for sub in orderdetails:
                total += sub.cost * sub.quantity
            return {'orderdetails': orderdetails,
                    'total':total}
        else:
            return {}
    else:
        return {}


# 123