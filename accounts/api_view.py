from.models import Property
from.serializer import PropertySerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView

# this is api decomation
# http://127.0.0.1:6589/api-documentation/



class PropertyAPiList(ListCreateAPIView):
    queryset=Property.objects.all()
    serializer_class = PropertySerializers
    permission_classes = [IsAuthenticated]


class PropertyAPiDetail(RetrieveUpdateDestroyAPIView):
    queryset=Property.objects.all()
    serializer_class = PropertySerializers
    permission_classes = [IsAuthenticated]