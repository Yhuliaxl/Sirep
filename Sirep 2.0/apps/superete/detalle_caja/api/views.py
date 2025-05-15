from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.superete.detalle_caja.models import DetalleCaja
from apps.superete.detalle_caja.api.serializers import DetalleCajaSerializer

class DetalleCajaViewSet(ModelViewSet):
    queryset = DetalleCaja.objects.all()
    serializer_class = DetalleCajaSerializer
    permission_classes = [IsAuthenticated]