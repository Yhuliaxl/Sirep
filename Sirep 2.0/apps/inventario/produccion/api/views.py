# apps/inventario/produccion/api/views.py
from apps.inventario.produccion.models import Produccion
from apps.inventario.produccion.api.serializers import ProduccionSerializer
from rest_framework.viewsets import ModelViewSet

class ProduccionViewSet(ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer