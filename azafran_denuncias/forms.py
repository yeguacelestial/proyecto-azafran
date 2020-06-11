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
        widgets = {'denuncia': forms.Textarea(attrs={'rows':5, 'cols':20, 'style':'resize: none'})}
    
    def __init__(self, *args, **kwargs):
        super(DenunciaForm, self).__init__(*args, **kwargs)
        self.fields['edad'].empty_label = "Selecciona una edad"
        self.fields['escuela'].empty_label = "Selecciona una institución"
        #self.fields['genero'].required = False