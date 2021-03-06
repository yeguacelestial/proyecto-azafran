from django.urls import path,include
from . import views
from azafran_denuncias.router import router # Required for API

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('denuncias', views.denuncias_list, name='denuncias'),
    path('testimonios/', views.DenunciasView.as_view(), name='denuncias'),
    path('alzalavoz', views.denuncias_form, name='denunciar'),
    path('testimonios/<int:pk>', views.DenunciaDetalladaView.as_view(), name='denuncia_detallada'),
    path('api/', include(router.urls)), # Including API URL
]