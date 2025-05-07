# apps/inventario/movimientos/api/serializers.py
from rest_framework import serializers
from apps.movimiento.movimientos.models import Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = [
            'id_movimiento', 'estado', 'fecha', 'fk_persona', 'tipo', 'num_factura'
        ]