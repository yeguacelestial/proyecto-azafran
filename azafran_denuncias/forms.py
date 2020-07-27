from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):

    class Meta:
        model = Denuncia
        #fields = '__all__'
        fields = ('edad', 'genero', 'denuncia')
        labels = {
            'edad': '¿Qué edad tenías cuando sucedió?',
            'genero': '¿Cuál es tu genero?',
            'denuncia': 'Mándanos tu testimonio, y #AlzaLaVoz.'
        }
        widgets = {'denuncia': forms.Textarea(attrs={'rows':5, 'cols':20, 'style':'resize: none'})}
    
    def __init__(self, *args, **kwargs):
        super(DenunciaForm, self).__init__(*args, **kwargs)
        self.fields['edad'].empty_label = "Selecciona un rango de edad"
        #self.fields['genero'].required = False