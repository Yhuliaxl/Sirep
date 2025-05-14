from rest_framework.viewsets import ModelViewSet
from apps.empresa.personas.models import persona
from rest_framework.permissions import IsAuthenticated
from apps.empresa.personas.api.serializers import personaSerializer

class personaViewSet(ModelViewSet):
    queryset = persona.objects.all()
    serializer_class =  personaSerializer 
    permission_classes = [IsAuthenticated]