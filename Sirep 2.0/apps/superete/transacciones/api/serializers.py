from rest_framework import serializers
from apps.superete.transacciones.models import Transaccion

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = [
            'tipo',
            'producto_id',
            'cantidad',
            'precio_unitario',
            'fecha',
            'persona_id',
        ]