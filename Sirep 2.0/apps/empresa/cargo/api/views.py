from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.empresa.cargo.models import cargo
from apps.empresa.cargo.api.serializers import cargoSerializer

class cargoViewSet(ModelViewSet):
    queryset = cargo.objects.all()
    serializer_class =  cargoSerializer