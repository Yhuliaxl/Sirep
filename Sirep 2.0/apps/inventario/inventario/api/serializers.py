from rest_framework import serializers
from apps.inventario.inventario.models import Inventario
from apps.inventario.productos.api.serializers import ProductoSerializer  # Asegúrate de que este serializer exista
from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer  # Asegúrate de que este serializer exista

class InventarioSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_codigo_pdto = serializers.PrimaryKeyRelatedField(
        queryset=Inventario._meta.get_field("fk_codigo_pdto").remote_field.model.objects.all(),
        write_only=True
    )
    fk_id_punto_vent = serializers.PrimaryKeyRelatedField(
        queryset=Inventario._meta.get_field("fk_id_punto_vent").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    producto = serializers.SerializerMethodField()
    punto_venta = serializers.SerializerMethodField()

    class Meta:
        model = Inventario
        fields = [
            'id_inventario',
            'fk_id_punto_vent',
            'fk_codigo_pdto',
            'cantidad',
            'fecha_actual',
            'producto',
            'punto_venta',
        ]

    def get_producto(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.inventario.productos.api.serializers import ProductoSerializer
        return ProductoSerializer(obj.fk_codigo_pdto).data if obj.fk_codigo_pdto else None

    def get_punto_venta(self, obj):
        from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer
        return PuntoVentaSerializer(obj.fk_id_punto_vent).data if obj.fk_id_punto_vent else None