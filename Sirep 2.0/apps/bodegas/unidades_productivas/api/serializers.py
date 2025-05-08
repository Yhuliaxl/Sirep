from rest_framework import serializers
from apps.bodegas.unidades_productivas.models import unidadProductiva

class unidadProductivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = unidadProductiva
        fields = [
            'codigo_up',
            'nombre',
            'logo',
            'descripcion',
            'sede',
            'estado',
            'entrega_producto',
            'fk_persona'
        ]
        read_only_fields = ['codigo_up']