from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

def Home(request):
    # You Are In Page Home
    context = {'name': 'Value from context'}
    return render(request, 'food/home.html',context)


def BookATable(request):
    # You Are In Page BookATable
    context = {'name': 'Value from context'}
    return render(request, 'pages/bookatable.html',context)



def Reservation(request):
    # You Are In Page Reservation
    context = {'name': 'Value from context'}
    return render(request, 'pages/reservation.html',context)


def AboutUs(request):
    # You Are In Page AboutUs
    context = {'name': 'Value from context'}
    return render(request, 'pages/aboutus.html',context)


def Contact(request):
    # You Are In Page Contact
    context = {'name': 'Value from context'}
    return render(request, 'pages/contact.html',context)



