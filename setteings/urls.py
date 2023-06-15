from django.urls import path
from . import views
app_name = 'setteings'

urlpatterns = [
    path('aboutus',views.AboutUs, name = 'aboutus'),
]

