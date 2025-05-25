from rest_framework import serializers
from apps.bodegas.punto_venta.models import PuntoVenta
from apps.empresa.personas.api.serializers import personaSerializer  # Asegúrate de que este serializer exista

class PuntoVentaSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    abierta_por = serializers.PrimaryKeyRelatedField(
        queryset=PuntoVenta._meta.get_field("abierta_por").remote_field.model.objects.all(),
        write_only=True
    )
    cerrada_por = serializers.PrimaryKeyRelatedField(
        queryset=PuntoVenta._meta.get_field("cerrada_por").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    abierta_por_data = serializers.SerializerMethodField()
    cerrada_por_data = serializers.SerializerMethodField()

    class Meta:
        model = PuntoVenta
        fields = [
            'id_punto_vent',
            'nombre',
            'estado',
            'fecha_apertura',
            'fecha_cierre',
            'saldo_inicial',
            'saldo_final',
            'observaciones',
            'abierta_por',
            'cerrada_por',
            'abierta_por_data',
            'cerrada_por_data',
        ]
        read_only_fields = ['id_punto_vent']

    def get_abierta_por_data(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.empresa.personas.api.serializers import personaSerializer
        return personaSerializer(obj.abierta_por).data if obj.abierta_por else None

    def get_cerrada_por_data(self, obj):
        from apps.empresa.personas.api.serializers import personaSerializer
        return personaSerializer(obj.cerrada_por).data if obj.cerrada_por else None