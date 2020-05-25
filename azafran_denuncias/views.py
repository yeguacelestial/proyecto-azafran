from django.shortcuts import render

# Create your views here.

# Testing
def testing(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de inicio
def inicio(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de protocolos
def protocolos(request):
    return render(request, 'azafran_denuncias/protocolos.html')

# Página de testimonios
def denuncias_list(request):
    return render(request, 'azafran_denuncias/testimonios.html')

# Formulario para crear denuncias
def denuncias_form(request):
    return render(request, 'azafran_denuncias/alza_la_voz.html')

# Eliminar un denuncia
def denuncia_delete(request):
    return