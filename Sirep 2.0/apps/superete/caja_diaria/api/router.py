from rest_framework.routers import DefaultRouter
from .views import CajaDiariaViewSet

cajaDiariaRouter = DefaultRouter()
cajaDiariaRouter.register(r'cajas', CajaDiariaViewSet)