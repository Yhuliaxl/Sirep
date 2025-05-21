from rest_framework import serializers
from apps.empresa.personas.models import persona
from apps.empresa.cargo.api.serializers import cargoSerializer  # Asegúrate de que este serializer exista

class personaSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    cargo = serializers.PrimaryKeyRelatedField(
        queryset=persona._meta.get_field("cargo").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    cargo_data = serializers.SerializerMethodField()

    class Meta:
        model = persona
        fields = [
            'nombre',
            'correo',
            'identificacion',
            'login',
            'password',
            'direccion',
            'telefono',
            'cargo',
            'rol',
            'ficha',
            'estado',
            'cargo_data',
        ]
        read_only_fields = ['identificacion']

    def get_cargo_data(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.empresa.cargo.api.serializers import cargoSerializer
        return cargoSerializer(obj.cargo).data if obj.cargo else None