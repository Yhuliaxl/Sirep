# apps/inventario/produccion/api/routers.py
from rest_framework.routers import DefaultRouter
from .views import ProduccionViewSet

produccionRouter = DefaultRouter()
produccionRouter.register(r'produccion', ProduccionViewSet)