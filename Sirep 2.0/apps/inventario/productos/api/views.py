# apps/inventario/productos/api/views.py
from apps.inventario.productos.models import Producto
from apps.inventario.productos.api.serializers import ProductoSerializer
from rest_framework.viewsets import ModelViewSet

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer