from rest_framework.routers import DefaultRouter
from .views import DetalleCajaViewSet

detalleCajaRouter = DefaultRouter()
detalleCajaRouter.register(r'detallecaja', DetalleCajaViewSet)