from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('denuncias', views.denuncias_list, name='denuncias'),
    path('alzalavoz', views.denuncias_form, name='denunciar'),
]