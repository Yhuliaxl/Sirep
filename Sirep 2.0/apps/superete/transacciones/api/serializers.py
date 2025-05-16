from rest_framework import serializers
from apps.superete.transacciones.models import Transaccion

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = [
            'id', 'caja_id', 'tipo', 'monto', 'descripcion',
            'fecha', 'creado', 'actualizado'
        ]