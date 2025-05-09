from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.bodegas.punto_venta.models import PuntoVenta
from apps.bodegas.punto_venta.api.serializers import PuntoVentaSerializer

class PuntoVentaViewSet(ModelViewSet):
    queryset = PuntoVenta.objects.all()
    serializer_class = PuntoVentaSerializer
     #token
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated] 