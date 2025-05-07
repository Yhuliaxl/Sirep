from rest_framework import serializers
from apps.empresa.cargo.models import cargo

class cargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cargo
        fields = [
            'id_sena',
            'nombre',
            'num_factura',
        ]
        read_only_fields = ['id_sena']