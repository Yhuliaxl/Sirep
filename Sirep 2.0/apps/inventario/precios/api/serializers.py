from rest_framework import serializers
from apps.inventario.precios.models import Precio
from apps.empresa.cargo.api.serializers import cargoSerializer  # Asegúrate de que este serializer exista
from apps.inventario.productos.api.serializers import ProductoSerializer  # Asegúrate de que este serializer exista

class PrecioSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    fk_cargo = serializers.PrimaryKeyRelatedField(
        queryset=Precio._meta.get_field("fk_cargo").remote_field.model.objects.all(),
        write_only=True
    )
    fk_producto = serializers.PrimaryKeyRelatedField(
        queryset=Precio._meta.get_field("fk_producto").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    cargo = serializers.SerializerMethodField()
    producto = serializers.SerializerMethodField()

    class Meta:
        model = Precio
        fields = [
            'id_precio',
            'fk_cargo',
            'fk_producto',
            'precio',
            'cargo',
            'producto',
        ]

    def get_cargo(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.empresa.cargo.api.serializers import cargoSerializer
        return cargoSerializer(obj.fk_cargo).data if obj.fk_cargo else None

    def get_producto(self, obj):
        from apps.inventario.productos.api.serializers import ProductoSerializer
        return ProductoSerializer(obj.fk_producto).data if obj.fk_producto else None