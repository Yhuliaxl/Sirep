from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.superete.caja_diaria.models import CajaDiaria
from apps.superete.caja_diaria.api.serializers import CajaDiariaSerializer

class CajaDiariaViewSet(ModelViewSet):
    queryset = CajaDiaria.objects.all()
    serializer_class = CajaDiariaSerializer
    permission_classes = [IsAuthenticated]