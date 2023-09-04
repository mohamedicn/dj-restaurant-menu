from rest_framework import serializers
from.models import Restaurantmenu,Order,OrderDetails


class FoodSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Restaurantmenu
        fields = "__all__"



class OrderSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Order
        fields = "__all__"
    
class OrderDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=OrderDetails
        # fields = "__all__"
        exclude = ('order','cost',)
        
    