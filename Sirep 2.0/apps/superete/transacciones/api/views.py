from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.superete.transacciones.models import Transacciones
from apps.superete.transacciones.api.serializers import TransaccionesSerializer

class TransaccionesViewSet(ModelViewSet):
    queryset = Transacciones.objects.all()
    serializer_class = TransaccionesSerializer
    permission_classes = [IsAuthenticated]