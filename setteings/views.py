from django.shortcuts import render
from.models import *

# Create your views here.


def AboutUs(request):
    # You in page About Us
    description = Description.objects.filter(active=True)
    ourTeam = OurTeam.objects.all()
    gallery = Gallery.objects.all()
    context = {'description': description,
                'OurTeam': ourTeam,
                'gallery': gallery,
            }
    return render(request, 'Pages/aboutUs.html', context)




# return HTTPResponse('Hello World')












