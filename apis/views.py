from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here

def home(request):
    stu=Students.objects.all()
    context = {
        'students':stu,
        'page_title': 'Aura Academy - Student Directory'
    }
    return render(request,'home.html',context)


def products(request):
    return render(request,'index.html')