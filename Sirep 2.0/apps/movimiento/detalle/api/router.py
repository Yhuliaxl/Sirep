from rest_framework.routers import DefaultRouter
from .views import DetalleViewSet

detalleRouter = DefaultRouter()
detalleRouter.register(r'detalle', DetalleViewSet)