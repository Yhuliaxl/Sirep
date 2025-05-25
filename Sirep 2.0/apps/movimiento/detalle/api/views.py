# apps/inventario/detalle/api/views.py
from apps.movimiento.detalle.models import DetalleProduccion
from apps.movimiento.detalle.api.serializers import DetalleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class DetalleViewSet(ModelViewSet):
    queryset = DetalleProduccion.objects.all()
    serializer_class = DetalleSerializer
    permission_classes = [IsAuthenticated]