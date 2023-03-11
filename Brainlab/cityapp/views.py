from django.shortcuts import render, HttpResponse
from faker import Faker
import requests
# Create your views here.


def randomcountry(request):
    if request.method == 'GET':
        fake = Faker()
        template_name = 'cityapp/home.html'
        context = {'country':fake.country()}
        return render(request,template_name,context)


def check(request):
    if request.method == 'POST':
        u = request.POST.get('Country')
        p = request.POST.get('Capital').title()
    
        r = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
        d=r.json()['data']
        template_name= 'cityapp/ans.html'
        for i in d:
            if i['name'] == u and i['capital'] == p:
                context={"msg":f"you are correct!! {p} is capital of {u}"}
                return render(request,template_name,context)
        for i in d:
            if i['name'] ==u:
                cap=i['capital']
                context={"msg":f"{p} is not capital of {u} correct Answer is {cap}"}
                print(context)
                return render(request,template_name,context)
