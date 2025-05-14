from rest_framework.routers import DefaultRouter
from .views import TransaccionesViewSet

TransaccionesRouter = DefaultRouter()
TransaccionesRouter.register(r'transacciones', TransaccionesViewSet)