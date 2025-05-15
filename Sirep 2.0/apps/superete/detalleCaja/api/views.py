from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.superete.detalleCaja.models import DetalleCaja
from apps.superete.detalleCaja.api.serializers import DetalleCajaSerializer

class DetalleCajaViewSet(ModelViewSet):
    queryset = DetalleCaja.objects.all()
    serializer_class = DetalleCajaSerializer
    permission_classes = [IsAuthenticated]