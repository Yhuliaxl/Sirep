# apps/inventario/inventario/serializers.py
from rest_framework import serializers
from apps.inventario.inventario.models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id_inventario', 'fk_id_punto_vent', 'fk_codigo_pdto', 'cantidad', 'fecha_actual']