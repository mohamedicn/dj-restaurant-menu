from django.shortcuts import render
from .models import Food
# Create your views here.


def RestMenu(request):
    # You Are In Page one Restaurant Menu
    context = {'name': 'Value from context'}
    return render(request, 'Food/RestMenu.html',context)


def RestMenus(request):
    # You Are In Page All Restaurant Menu
    data = Food.objects.all()
    context = {'food': data}
    return render(request, 'Food/RestMenus.html',context)


