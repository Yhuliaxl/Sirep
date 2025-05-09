from rest_framework import serializers
from apps.bodegas.bodega.models import Bodega


class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = [
            'id_bodega',
            'fecha',
            'cantidad',
            'fk_inventario',
            'fk_produccion',
        ]
        read_only_fields = ['id_bodega']
