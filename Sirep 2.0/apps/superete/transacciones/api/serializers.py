from rest_framework import serializers
from apps.superete.transacciones.models import Transacciones

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = [
            'id', 'caja_id', 'tipo', 'monto', 'descripcion',
            'fecha', 'creado', 'actualizado'
        ]