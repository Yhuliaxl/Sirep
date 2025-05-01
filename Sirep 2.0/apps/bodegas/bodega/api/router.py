from rest_framework.routers import DefaultRouter
from .views import BodegaViewSet

Bodegarouter = DefaultRouter()
Bodegarouter.register(r'bodegas', BodegaViewSet, basename='bodega')

urlpatterns = Bodegarouter.urls 
