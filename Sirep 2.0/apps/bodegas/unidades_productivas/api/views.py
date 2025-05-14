from rest_framework.viewsets import ModelViewSet
from apps.bodegas.unidades_productivas.models import unidadProductiva
from rest_framework.permissions import IsAuthenticated
from apps.bodegas.unidades_productivas.api.serializers import unidadProductivaSerializer

class unidadProductivaViewSet(ModelViewSet):
    queryset = unidadProductiva.objects.all()
    serializer_class = unidadProductivaSerializer
    permission_classes = [IsAuthenticated]