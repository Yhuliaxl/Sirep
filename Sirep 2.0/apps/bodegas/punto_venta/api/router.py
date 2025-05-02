from rest_framework.routers import DefaultRouter
from .views import PuntoVentaViewSet

puntoVentaRouter = DefaultRouter()
puntoVentaRouter.register(r'puntoventa', PuntoVentaViewSet, basename='puntoventa')

urlpatterns = puntoVentaRouter.urls 