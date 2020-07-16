from django.shortcuts import render, redirect

from .forms import DenunciaForm
from .models import Denuncia
from .models import DenunciaPublicada

# For listing denuncias
"""
    ListView: List all denuncias
    DetailView: List a single denuncia
"""
from django.views.generic import ListView, DetailView

# Create your views here.

# Testing
def testing(request):
    return render(request, 'azafran_denuncias/testing.html')

# Página de inicio
def inicio(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de protocolos
def protocolos(request):
    return render(request, 'azafran_denuncias/protocolos.html')

# Página de testimonios
# def denuncias_list(request):
#     context = {'denuncias_list': Denuncia.objects.all()}
#     return render(request, 'azafran_denuncias/testimonios.html', context)

# Formulario para crear denuncias
def denuncias_form(request):
    if request.method == 'GET':
        form = DenunciaForm()
        return render(request, 'azafran_denuncias/alza_la_voz.html', {'form': form})
    else:
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/testimonios')

# Eliminar un denuncia
def denuncia_delete(request):
    return

# Desplegar todas las denuncias
class DenunciasView(ListView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/testimonios.html'

# Vista detallada de denuncia
class DenunciaDetalladaView(DetailView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/denuncia.html'