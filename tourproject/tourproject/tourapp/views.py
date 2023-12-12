from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import people


# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=people.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})

#def addition(request):
 #   x=(request.GET['num1'])
  #  y=(request.GET['num2'])
   # res=x+y
    #return render(request,'about.html',{'result':res})