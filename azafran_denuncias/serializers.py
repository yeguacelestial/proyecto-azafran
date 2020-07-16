from rest_framework import serializers
from .models import Denuncia, DenunciaPublicada

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class DenunciaPublicadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DenunciaPublicada
        fields = '__all__'