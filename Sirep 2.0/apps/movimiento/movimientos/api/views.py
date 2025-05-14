# apps/inventario/movimientos/api/views.py
from apps.movimiento.movimientos.models import Movimiento
from apps.movimiento.movimientos.api.serializers import MovimientoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class MovimientoViewSet(ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [IsAuthenticated]