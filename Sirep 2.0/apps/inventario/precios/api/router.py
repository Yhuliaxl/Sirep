# apps/inventario/inventario/routers.py
from rest_framework.routers import DefaultRouter
from .views import PrecioViewSet

preciosRouter = DefaultRouter()
preciosRouter.register(r'precio', PrecioViewSet)