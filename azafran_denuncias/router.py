from azafran_denuncias.viewsets import DenunciaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('denuncia', DenunciaViewset)