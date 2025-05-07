from rest_framework import serializers
from apps.empresa.sena_empresa.models import senaEmpresa

class senaEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = senaEmpresa
        fields = [
            'id_sena',
            'nombre',
            'num_factura',
        ]
        read_only_fields = ['id_sena']