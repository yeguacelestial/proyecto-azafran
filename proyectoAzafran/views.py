from django.shortcuts import render
from django.http import HttpResponse

# Función principal
def home(request):
    return render(request, 'base.html')

def azafran(request):
    return HttpResponse("view azafran")