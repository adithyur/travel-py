from django.http import HttpResponse
from django.shortcuts import render

from . models import Guide
from . models import Place

# Create your views here.

def demo(request):
    obj=Guide.objects.all()

    obj1=Place.objects.all()
    return render(request,"index.html",{'result':obj, 'product':obj1})

def about(request):
    return render(request,"about.html")

# def addition(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     c=a+b
#     d=a*b
#     e=a-b
#     f=a/b
#     return render(request,"add.html",{'obj':c,'obj1':d,'obj2':e,'obj3':f})