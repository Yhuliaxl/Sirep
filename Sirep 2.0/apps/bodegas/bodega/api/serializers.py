from rest_framework import serializers
from apps.bodegas.bodega.models import Bodega

class BodegaSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_inventario = serializers.PrimaryKeyRelatedField(
        queryset=Bodega._meta.get_field("fk_inventario").remote_field.model.objects.all(),
        write_only=True
    )
    fk_detalle_produccion = serializers.PrimaryKeyRelatedField(
        queryset=Bodega._meta.get_field("fk_detalle_produccion").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    inventario = serializers.SerializerMethodField()
    detalle_produccion = serializers.SerializerMethodField()

    class Meta:
        model = Bodega
        fields = [
            'id_bodega',
            'fecha',
            'cantidad',
            'fk_inventario',
            'fk_detalle_produccion',
            'inventario',
            'detalle_produccion',
        ]
        read_only_fields = ['id_bodega']

    def get_inventario(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.inventario.inventario.api.serializers import InventarioSerializer
        if obj.fk_inventario:
            serializer = InventarioSerializer(obj.fk_inventario)
            return serializer.data
        return None

    def get_detalle_produccion(self, obj):
        from apps.movimiento.detalle.api.serializers import DetalleSerializer
        if obj.fk_detalle_produccion:
            serializer = DetalleSerializer(obj.fk_detalle_produccion)
            return serializer.data
        return None