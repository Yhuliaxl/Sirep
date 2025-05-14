from rest_framework.viewsets import ModelViewSet
from apps.empresa.cargo.models import cargo
from rest_framework.permissions import IsAuthenticated

from apps.empresa.cargo.api.serializers import cargoSerializer

class cargoViewSet(ModelViewSet):
    queryset = cargo.objects.all()
    serializer_class =  cargoSerializer
    permission_classes = [IsAuthenticated]

    