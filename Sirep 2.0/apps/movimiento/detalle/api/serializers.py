from rest_framework import serializers
from apps.movimiento.detalle.models import DetalleProduccion
from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer  # Asegúrate de que este serializer exista
from apps.movimiento.movimientos.api.serializers import MovimientoSerializer  # Asegúrate de que este serializer exista
from apps.inventario.inventario.api.serializers import InventarioSerializer  # Asegúrate de que este serializer exista
from apps.inventario.productos.api.serializers import ProductoSerializer  # Asegúrate de que este serializer exista

class DetalleSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_punto_venta_caja = serializers.PrimaryKeyRelatedField(
        queryset=DetalleProduccion._meta.get_field("fk_punto_venta_caja").remote_field.model.objects.all(),
        write_only=True
    )
    fk_movimiento_transaccion = serializers.PrimaryKeyRelatedField(
        queryset=DetalleProduccion._meta.get_field("fk_movimiento_transaccion").remote_field.model.objects.all(),
        write_only=True
    )
    fk_inventario = serializers.PrimaryKeyRelatedField(
        queryset=DetalleProduccion._meta.get_field("fk_inventario").remote_field.model.objects.all(),
        write_only=True
    )
    fk_producto = serializers.PrimaryKeyRelatedField(
        queryset=DetalleProduccion._meta.get_field("fk_producto").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    punto_venta_caja = serializers.SerializerMethodField()
    movimiento_transaccion = serializers.SerializerMethodField()
    inventario = serializers.SerializerMethodField()
    producto = serializers.SerializerMethodField()

    class Meta:
        model = DetalleProduccion
        fields = [
            'id_detalle',
            'tipo_movimiento',
            'cantidad',
            'valor',
            'persona',
            'descripcion',
            'fecha',
            'observacion',
            'fk_punto_venta_caja',
            'fk_movimiento_transaccion',
            'fk_inventario',
            'fk_producto',
            'punto_venta_caja',
            'movimiento_transaccion',
            'inventario',
            'producto',
        ]
        read_only_fields = ['id_detalle']

    def get_punto_venta_caja(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer
        return PuntoVentaSerializer(obj.fk_punto_venta_caja).data if obj.fk_punto_venta_caja else None

    def get_movimiento_transaccion(self, obj):
        from apps.movimiento.movimientos.api.serializers import MovimientoSerializer
        return MovimientoSerializer(obj.fk_movimiento_transaccion).data if obj.fk_movimiento_transaccion else None

    def get_inventario(self, obj):
        from apps.inventario.inventario.api.serializers import InventarioSerializer
        return InventarioSerializer(obj.fk_inventario).data if obj.fk_inventario else None

    def get_producto(self, obj):
        from apps.inventario.productos.api.serializers import ProductoSerializer
        return ProductoSerializer(obj.fk_producto).data if obj.fk_producto else None