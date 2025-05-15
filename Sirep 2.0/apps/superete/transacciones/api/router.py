from rest_framework.routers import DefaultRouter
from .views import TransaccionesViewSet

transaccionesRouter = DefaultRouter()
transaccionesRouter.register(r'transacciones', TransaccionesViewSet)