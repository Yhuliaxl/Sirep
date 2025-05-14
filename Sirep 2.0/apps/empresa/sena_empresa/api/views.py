from rest_framework.viewsets import ModelViewSet
from apps.empresa.sena_empresa.models import senaEmpresa
from rest_framework.permissions import IsAuthenticated
from apps.empresa.sena_empresa.api.serializers import senaEmpresaSerializer

class SenaEmpresaViewSet(ModelViewSet):
    queryset = senaEmpresa.objects.all()
    serializer_class = senaEmpresaSerializer 
    permission_classes = [IsAuthenticated]