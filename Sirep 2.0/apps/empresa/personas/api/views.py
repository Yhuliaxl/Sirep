from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.empresa.personas.models import persona
from apps.empresa.personas.api.serializers import personaSerializer

class personaViewSet(ModelViewSet):
    queryset = persona.objects.all()
    serializer_class =  personaSerializer
    #token
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated] 