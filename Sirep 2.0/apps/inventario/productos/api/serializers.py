# apps/inventario/productos/api/serializers.py
from rest_framework import serializers
from apps.inventario.productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'codigo_pdto', 'nombre', 'descripcion', 'imagen', 'estado', 'reserva',
            'max_reserva', 'tipo', 'hora_inicio', 'hora_fin', 'inventario', 'fk_codigo_up'
        ]