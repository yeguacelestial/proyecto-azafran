from django.shortcuts import render
from django.http import HttpResponse


def maintainment(request):
    return render(request, 'mnt.html')

# Función principal
def home(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')
    
def azafran(request):
    return HttpResponse("view azafran")