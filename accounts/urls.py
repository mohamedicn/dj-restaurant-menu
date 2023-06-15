from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='accounts'


urlpatterns = [
    path('signin',views.signin ,name='signin'),
    path('log_out',views.log_out ,name='log_out'),
    path('productfavorites/<str:slug>',views.product_favorites ,name='product_favorites'),
    path('product-favorites',views.showproduct_favorites ,name='showproduct_favorites'),
]
