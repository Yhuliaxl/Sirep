from rest_framework import serializers
from apps.movimiento.movimientos.models import Movimiento
from apps.empresa.personas.api.serializers import personaSerializer  # Asegúrate de que este serializer exista
from apps.inventario.productos.api.serializers import ProductoSerializer  # Asegúrate de que este serializer exista

class MovimientoSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_persona = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento._meta.get_field("fk_persona").remote_field.model.objects.all(),
        write_only=True
    )
    fk_producto = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento._meta.get_field("fk_producto").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    persona = serializers.SerializerMethodField()
    producto = serializers.SerializerMethodField()

    class Meta:
        model = Movimiento
        fields = [
            'id_movimiento',
            'tipo_movimiento',
            'cantidad',
            'precio_unitario',
            'fecha',
            'num_factura',
            'fk_persona',
            'fk_producto',
            'persona',
            'producto',
        ]
        read_only_fields = ['id_movimiento']

    def get_persona(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.empresa.personas.api.serializers import personaSerializer
        return personaSerializer(obj.fk_persona).data if obj.fk_persona else None

    def get_producto(self, obj):
        from apps.inventario.productos.api.serializers import ProductoSerializer
        return ProductoSerializer(obj.fk_producto).data if obj.fk_producto else None