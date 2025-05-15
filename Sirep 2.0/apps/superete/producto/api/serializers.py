from rest_framework import serializers
from apps.superete.producto.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = [
            'id', 'nombre', 'categoria_id', 'precio_compra', 'precio_venta',
            'stock', 'creado', 'actualizado'
        ]