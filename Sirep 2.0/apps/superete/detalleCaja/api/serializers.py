from rest_framework import serializers
from apps.superete.detalleCaja.models import DetalleCaja

class DetalleCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCaja
        fields = [
            'id', 'nombre', 'fecha_apertura', 'fecha_cierre', 'saldo_inicial',
            'saldo_final', 'abierta_por', 'cerrada_por', 'observaciones',
            'creado', 'actualizado'
        ]