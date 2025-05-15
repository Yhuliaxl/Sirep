from rest_framework import serializers
from apps.superete.detalle_caja.models import DetalleCaja

class DetalleCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCaja
        fields = [
            'id',
            'caja_id',
            'transaccion_id',
            'descripcion',
            'tipo',
            'monto',
            'fecha',
            #'caja',
            #'transaccion'
        ]