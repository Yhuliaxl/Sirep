from rest_framework.viewsets import ModelViewSet
from apps.empresa.sena_empresa.models import senaEmpresa
from apps.empresa.sena_empresa.api.serializers import senaEmpresaSerializer

class SenaEmpresaViewSet(ModelViewSet):
    queryset = senaEmpresa.objects.all()
    serializer_class = senaEmpresaSerializer 