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

# Formulario para crear denuncias
def denuncias_form(request):
    denuncia_model = Denuncia()

    if request.method == 'GET':
        form = DenunciaForm()
        return render(request, 'azafran_denuncias/alza_la_voz.html', {'form': form})

    else:
        form = DenunciaForm(request.POST)

        if form.is_valid():
            form.save()

            # Getting client's ip
            from ipware import get_client_ip
            ip, is_routable = get_client_ip(request)
            if ip is None:
                print('Unable to get client\'s ip ')
            else:
                if is_routable:
                    print(f'IP is routable => {ip}')

                else:
                    print(f'Client\'s IP is not routable (IP => {ip})')

                    # Storing client's IP on database
                    denuncia_model.ip_publica_testimonio = ip

            # Save model
            denuncia_model.save()

            # Redirect to testimonios page
            return redirect('/testimonios')


# Desplegar todas las denuncias
class DenunciasView(ListView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/testimonios.html'

# Vista detallada de denuncia
class DenunciaDetalladaView(DetailView):
    model = DenunciaPublicada
    template_name = 'azafran_denuncias/denuncia.html'