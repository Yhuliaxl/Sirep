from rest_framework import serializers
from apps.bodegas.punto_venta.models import PuntoVenta

class PuntoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoVenta
        fields = [
            'id_punto_vent',
            'sede',
            'direccion',
            'nombre',
            #'Fk_persona',
            'estado'
        ]
        read_only_fields = ['Id_punto_vent']