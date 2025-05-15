from rest_framework import serializers
from apps.superete.caja_diaria.models import CajaDiaria

class CajaDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CajaDiaria
        fields = [
            'id', 'nombre', 'fecha_apertura', 'fecha_cierre', 'saldo_inicial',
            'saldo_final', 'abierta_por', 'cerrada_por', 'observaciones'
        ]