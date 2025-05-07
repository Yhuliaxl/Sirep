# apps/inventario/productos/api/routers.py
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

productosRouter = DefaultRouter()
productosRouter.register(r'producto', ProductoViewSet)