from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'home.html', {'name':'dixit'})  

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'add_result': res})


#activate env we use command : workon env_name
#for start server we use commend : python manage.py runserver
