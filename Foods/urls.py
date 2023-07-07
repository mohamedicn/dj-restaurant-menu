from django.urls import path
from . import views


urlpatterns = [
    path('restMenus/',views.RestMenus, name = 'restMenus'),
    path('restMenus/restMenu',views.RestMenu, name = 'restMenu'),
]
