from.models import Restaurantmenu,Order,OrderDetails
from.serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404,get_object_or_404
from django.utils import timezone
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveAPIView, CreateAPIView

# this is api decomation
# http://127.0.0.1:6589/api-documentation/



class FoodAPiList(ListCreateAPIView):
    queryset=Restaurantmenu.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class FoodAPiDetail(RetrieveUpdateDestroyAPIView):
    queryset=Restaurantmenu.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]
    
# _______________     order api    ______

class OrderAPiList(ListCreateAPIView):
    # queryset=Order.objects.filter(user=request.user)
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Access the request user through self.request.user
        return Order.objects.filter(user=self.request.user)
class OrderDetailsByOrderIdAPIView(ListAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the order ID from the URL parameters
        order_id = self.kwargs['order_id']
        # Filter OrderDetails by the order ID
        return OrderDetails.objects.filter(order_id=order_id)
    
    
    
class AddToCartAPIView(RetrieveAPIView, CreateAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'order_id'

    def get_queryset(self):
        # Get the order ID from the URL parameters
        order_id = self.kwargs['order_id']
        # Filter OrderDetails by the order ID, and return at most one instance
        return OrderDetails.objects.filter(order_id=order_id, order__is_finished=False).last()

    def create(self, request, *args, **kwargs):
        # You can add custom logic here to create a new OrderDetails instance
        # based on the request data.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Ensure that you set the order_id to the value from the URL
        order_id = self.kwargs['order_id']
        serializer.validated_data['order_id'] = order_id
        
        product = serializer.validated_data.get('product')
        quantity = serializer.validated_data.get('quantity')
        if product:
            # Assuming the product has a 'price' field that represents its cost
            cost = product.Price
            serializer.validated_data['cost'] = cost

        # Check if an OrderDetails object with the same product exists for the order
        existing_order_details = OrderDetails.objects.filter(order_id=order_id, product=product).last()
        
        if existing_order_details:
            # If an existing record is found, update the quantity
            existing_order_details.quantity += quantity
            existing_order_details.save()
        else:
            # If no existing record is found, create a new one
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


