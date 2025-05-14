from rest_framework.viewsets import ModelViewSet
from apps.bodegas.punto_venta.models import PuntoVenta
from rest_framework.permissions import IsAuthenticated
from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer

class PuntoVentaViewSet(ModelViewSet):
    queryset = PuntoVenta.objects.all()
    serializer_class = PuntoVentaSerializer
    permission_classes = [IsAuthenticated]