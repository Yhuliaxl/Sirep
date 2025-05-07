# apps/inventario/detalle/api/serializers.py
from rest_framework import serializers
from apps.movimiento.detalle.models import Detalle

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = [
            'id_detalle', 'cantidad', 'valor', 'estado', 'entregado',
            'persona', 'fk_id_movimiento', 'fk_id_inventario'
        ]