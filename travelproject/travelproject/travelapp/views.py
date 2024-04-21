from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.

def demo(request):
    obj = Place.objects.all()
    new_obj = Team.objects.all()
    return render(request,"index.html",{'result':obj,'new_result':new_obj})


# def demo(request):
#     name="india"
#     return render(request,'index.html',{'obj':name})

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add= x + y
#     sub = x - y
#     mult = x*y
#     div = x/y
#     return render(request,"result.html",{'sum':add,'difference':sub,'product':mult,'division':div})


# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return render(request,'contact.html')
#
