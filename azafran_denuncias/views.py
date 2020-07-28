from django.shortcuts import render, redirect

from .forms import DenunciaForm
from .models import Denuncia
from .models import DenunciaPublicada

from ipware import get_client_ip

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

# Formulario para crear denuncias
def denuncias_form(request):
    if request.method == 'GET':
        form = DenunciaForm()
        return render(request, 'azafran_denuncias/alza_la_voz.html', {'form': form})

    else:
        form = DenunciaForm(request.POST)
        form.Meta().model.ip_publica_testimonio = get_public_ip(request)
        form.save()

        # Redirect to testimonios page
        return redirect('/testimonios')

# Capturar IP Pública del usuario
def get_public_ip(request):
    # Getting client's ip
    ip, is_routable = get_client_ip(request)

    if ip is None:
        print('Unable to get client\'s ip ')
        return 'IP no disponible'

    else:
        if is_routable:
            print(f'IP is routable => {ip}')
        else:
            print(f'Client\'s IP is not routable (IP => {ip})')
        return ip
    

# Desplegar todas las denuncias
class DenunciasView(ListView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/testimonios.html'

# Vista detallada de denuncia
class DenunciaDetalladaView(DetailView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/denuncia.html'