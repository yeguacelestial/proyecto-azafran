from django.shortcuts import render

# Create your views here.

# Testing
def testing(request):
    return render(request, 'mdbootstrap.html')

# Lista de denuncias actuales
def denuncias_list(request):
    return

# Formulario para crear denuncias
def denuncias_form(request):
    return

# Eliminar un denuncia
def denuncia_delete(request):
    return