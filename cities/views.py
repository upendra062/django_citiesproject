from django.shortcuts import render
from .models import Cities
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import requests

def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    # print(users)
    # return HttpResponse("Users")
    template = loader.get_template("apidata.html")
    context = {'allUsers':users}
    return HttpResponse(template.render(context, request))

def users1(request):
    #pull data from third party rest api
    response = requests.get('https://reqres.in/api/users')
    #convert reponse data into json
    users = response.json()
    # print(users)
    template = loader.get_template("apidata1.html")
    context = {'allUsers':users}
    return HttpResponse(template.render(context, request))

def cities(request):
    # x = Cities.objects.values('firstname', 'Mohan')
    #### descending order '-'
    x = Cities.objects.all().order_by('-firstname').values()
    #### arrange in asscending order
    # x = Cities.objects.all().order_by('firstname').values()
    #### firstname endswith a
    # x = Cities.objects.filter(firstname__endswith='a').values()
    #### firstname startswith 'R'
    # x = Cities.objects.filter(firstname__startswith='R').values()
    #### firstname is Mohan
    # x = Cities.objects.filter(firstname='Mohan').values()
    #### fetch all values
    # x = Cities.objects.all().values()
    ####
    # x = Cities.objects.filter(id='1').values() | Cities.objects.filter(id='2').values()
    
    context = {'data':x}
    return render(request, 'cities.html', context)

def details(request, id):
    x = Cities.objects.get(id=id)
    context = {'data':x}
    return render(request, 'details.html', context)

def last(request, id):
    x = Cities.objects.get(id=id)
    context = {"data":x}
    return render(request, 'last.html', context)

def template(request):
    # context = {'fname': 'Jack Sparrow'}
    # return render(request, 'template.html', context)

    # template = loader.get_template('template.html')
    # context = {
    #     'fname': 'Jack Sparrow'
    #     }
    # return HttpResponse(template.render(context, request))
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

def template2(request):
    template = loader.get_template('template2.html')
    context = {
        # 'fname': 'French'
        # 'fname': 'Jack Sparrow'
        # 'fname': 'Pan Singh Tomar'
        # 'language': "French",
        # 'age': 20
        # 'cityArr': ['Rampur', 'Dehli', 'Goa', 'Noida']
        
        'cityArr': [
            {
                "cityName": "Delhi",
                "age": '200',
            },
            {
                "cityName": "Noida",
                "age": '59',
            },
            {
                "cityName": "Mumbai",
                "age": '100',
            }]
        }
    return HttpResponse(template.render(context,request))

def newdynamic(request):
    x = Cities.objects.all()
    context = {'data':x}
    return render(request, 'newdynamic.html', context)
































