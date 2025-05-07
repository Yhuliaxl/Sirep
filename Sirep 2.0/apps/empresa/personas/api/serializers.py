from rest_framework import serializers
from apps.empresa.personas.models import persona

class personaSerializer(serializers.ModelSerializer):
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
            #'cargo',
            'rol',
            'ficha',
            'estado',
        ]
        read_only_fields = ['id_sena']