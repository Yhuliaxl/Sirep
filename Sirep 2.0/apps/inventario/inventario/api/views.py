# apps/inventario/productos/api/views.py
from apps.inventario.inventario.models import Inventario
from apps.inventario.inventario.api.serializers import InventarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class InventarioViewSet(ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]