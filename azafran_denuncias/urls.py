from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('denuncias', views.denuncias_list, name='denuncias'),
    path('denuncias/', views.DenunciasView.as_view(), name='denuncias'),
    path('alzalavoz', views.denuncias_form, name='denunciar'),
    path('denuncias/<int:pk>', views.DenunciaDetalladaView.as_view(), name='denuncia_detallada'),
]