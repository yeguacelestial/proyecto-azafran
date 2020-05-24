from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.testing),
    path('denuncias', views.denuncias_list)
]