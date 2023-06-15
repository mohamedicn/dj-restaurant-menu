from django.urls import path
from . import views
app_name='payment'
urlpatterns= [
    path('payment',views.Payment, name ='payment')
]