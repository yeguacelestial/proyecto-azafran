from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):

    class Meta:
        model = Denuncia
        #fields = '__all__'
        fields = ('edad', 'genero', 'escuela', 'denuncia')
        labels = {
            'edad': '¿Cuál es tu edad?',
            'genero': '¿Cuál es tu genero?',
            'escuela': '¿Perteneces a alguna de las siguientes instituciones?',
            'denuncia': 'Alza la voz.'
        }