from apps.inventario.precios.models import Precio
from apps.inventario.precios.api.serializers import PrecioSerializer
from rest_framework.viewsets import ModelViewSet

class PrecioViewSet(ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer