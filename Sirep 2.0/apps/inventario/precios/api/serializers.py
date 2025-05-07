# apps/inventario/precios/serializers.py
from rest_framework import serializers
from apps.inventario.precios.models import Precio

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ['id_precio', 'fk_cargo', 'fk_producto', 'precio']