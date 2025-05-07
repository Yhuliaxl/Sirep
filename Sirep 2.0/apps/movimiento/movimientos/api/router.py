# apps/inventario/movimientos/api/routers.py
from rest_framework.routers import DefaultRouter
from .views import MovimientoViewSet

movimientosRouter = DefaultRouter()
movimientosRouter.register(r'movimiento', MovimientoViewSet)