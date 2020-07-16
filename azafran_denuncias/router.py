from azafran_denuncias.viewsets import DenunciaViewset, DenunciaPublicadaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('denuncias_recibidas', DenunciaViewset)
router.register('denuncias_publicadas', DenunciaPublicadaViewset)