# apps.inventario.bodega.api.views.py
from rest_framework.viewsets import ModelViewSet
from apps.bodegas.bodega.models import Bodega
from apps.bodegas.bodega.api.serializers import BodegaSerializer

class BodegaViewSet(ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer