from rest_framework.routers import DefaultRouter
from .views import personaViewSet

personaRouter = DefaultRouter()
personaRouter.register(r'persona', personaViewSet, basename='persona')
