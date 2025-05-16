from rest_framework.routers import DefaultRouter
from .views import ProductosViewSet

productoRouter = DefaultRouter()
productoRouter.register(r'producto', ProductosViewSet)