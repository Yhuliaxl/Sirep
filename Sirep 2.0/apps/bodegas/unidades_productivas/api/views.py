from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.bodegas.unidades_productivas.models import unidadProductiva
from apps.bodegas.unidades_productivas.api.serializers import unidadProductivaSerializer

class unidadProductivaViewSet(ModelViewSet):
    queryset = unidadProductiva.objects.all()
    serializer_class = unidadProductivaSerializer