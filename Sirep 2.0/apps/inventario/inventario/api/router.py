# apps/inventario/inventario/routers.py
from rest_framework.routers import DefaultRouter
from .views import InventarioViewSet

# Configurar el router para las vistas basadas en ViewSet
inventarioRouter = DefaultRouter()
inventarioRouter.register(r'inventario', InventarioViewSet)