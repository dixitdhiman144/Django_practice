from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'home.html', {'name':'dixit'})  




#activate env we use command : workon env_name
#for start server we use commend : python manage.py runserver
