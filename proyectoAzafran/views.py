from django.shortcuts import render
from django.http import HttpResponse

# Función principal
def maintainment(request):
    return render(request, 'mnt.html')
    
def home(request):
    return render(request, 'base.html')

def azafran(request):
    return HttpResponse("view azafran")