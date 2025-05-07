# apps/inventario/produccion/api/serializers.py
from rest_framework import serializers
from apps.inventario.produccion.models import Produccion

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = ['id_produccion', 'estado', 'cantidad', 'fecha', 'observacion', 'fk_codigo_pdto']