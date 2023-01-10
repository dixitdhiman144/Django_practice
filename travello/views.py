from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Haryana'
    dest1.price = 755
    dest1.desc = 'States of Wrestlers and Boxers'
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'Karnataka'
    dest2.price = 955
    dest2.desc = 'First states of India where electricity comes'
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'Chandigarh'
    dest3.price = 855
    dest3.desc = 'The Beautiful City'
    dest3.img = 'destination_3.jpg'

    dests = [dest1,dest2,dest3]

    return render(request, "index.html", {'dests':dests})