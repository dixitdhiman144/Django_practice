from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Haryana'
    dest1.price = 755
    dest1.desc = 'The Wonderfull State'
    
    return render(request, "index.html", {'dest1':dest1})