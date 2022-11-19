from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fun1(request):
    return HttpResponse("created a page")

def home(request):
    return render(request,'home.html')

def img(request):
    return render(request,'img.html')
    
def about(request):
    return render(request,'about.html')