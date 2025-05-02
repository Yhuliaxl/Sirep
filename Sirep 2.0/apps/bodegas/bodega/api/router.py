from rest_framework.routers import DefaultRouter
from .views import BodegaViewSet

bodegaRouter = DefaultRouter()
bodegaRouter.register(r'bodegas', BodegaViewSet, basename='bodega')

urlpatterns = bodegaRouter.urls 
