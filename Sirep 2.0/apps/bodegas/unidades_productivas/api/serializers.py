from rest_framework import serializers
from apps.bodegas.unidades_productivas.models import unidadProductiva
from apps.empresa.personas.api.serializers import personaSerializer  # Asegúrate de que este serializer exista
#from apps.empresa.sena_empresa.api.serializers import senaEmpresaSerializer  # Asegúrate de que este serializer exista

class unidadProductivaSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_persona = serializers.PrimaryKeyRelatedField(
        queryset=unidadProductiva._meta.get_field("fk_persona").remote_field.model.objects.all(),
        write_only=True
    )
    #fk_sena_empresa = serializers.PrimaryKeyRelatedField(
     #   queryset=unidadProductiva._meta.get_field("fk_sena_empresa").remote_field.model.objects.all(),
    #    write_only=True
    #)
    # Para lectura: definimos campos calculados
    persona = serializers.SerializerMethodField()
    #sena_empresa = serializers.SerializerMethodField()

    class Meta:
        model = unidadProductiva
        fields = [
            'codigo_up',
            'nombre',
            'logo',
            'descripcion',
            'estado',
            'fk_persona',
            #'fk_sena_empresa',
            'persona',
            #'sena_empresa',
        ]
        read_only_fields = ['codigo_up']

    def get_persona(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.empresa.personas.api.serializers import personaSerializer
        return personaSerializer(obj.fk_persona).data if obj.fk_persona else None

    #def get_sena_empresa(self, obj):
       # from apps.empresa.sena_empresa.api.serializers import senaEmpresaSerializer
       # return senaEmpresaSerializer(obj.fk_sena_empresa).data if obj.fk_sena_empresa else None