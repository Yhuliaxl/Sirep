from rest_framework import serializers
from apps.superete.categoria.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id', 'nombre', 'descripcion', 'creado', 'actualizado'
        ]