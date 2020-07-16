from rest_framework import viewsets
from . import models
from . import serializers

class DenunciaViewset(viewsets.ModelViewSet):
    queryset = models.Denuncia.objects.all()
    serializer_class = serializers.DenunciaSerializer

class DenunciaPublicadaViewset(viewsets.ModelViewSet):
    queryset = models.DenunciaPublicada.objects.all()
    serializer_class = serializers.DenunciaPublicadaSerializer