from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.empresa.sena_empresa.models import senaEmpresa
from apps.empresa.sena_empresa.api.serializers import senaEmpresaSerializer

class SenaEmpresaViewSet(ModelViewSet):
    queryset = senaEmpresa.objects.all()
    serializer_class = senaEmpresaSerializer 
     #token
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated] 