# apps/inventario/inventario/serializers.py
from rest_framework import serializers
from apps.inventario.inventario.models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id_inventario', 'id_bodega', 'id_producto', 'cantidad', 'fecha_actual']