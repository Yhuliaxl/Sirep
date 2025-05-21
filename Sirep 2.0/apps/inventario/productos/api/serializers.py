from rest_framework import serializers
from apps.inventario.productos.models import Producto
from apps.superete.categoria.api.serializers import CategoriaSerializer  # Asegúrate de que este serializer exista

class ProductoSerializer(serializers.ModelSerializer):
    # Para escritura: se envían solo los IDs
    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Producto._meta.get_field("categoria").remote_field.model.objects.all(),
        write_only=True
    )
    # Para lectura: definimos campos calculados
    categoria_data = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = [
            'codigo_pdto',
            'nombre',
            'descripcion',
            'imagen',
            'estado',
            'tipo',
            'precio_compra',
            'precio_venta',
            'stock',
            'categoria',
            'categoria_data',
        ]
        read_only_fields = ['codigo_pdto']

    def get_categoria_data(self, obj):
        # Importamos localmente para evitar problemas de importación circular
        from apps.superete.categoria.api.serializers import CategoriaSerializer
        return CategoriaSerializer(obj.categoria).data if obj.categoria else None