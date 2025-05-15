from rest_framework.routers import DefaultRouter
from .views import ProductosViewSet

ProductosRouter = DefaultRouter()
ProductosRouter.register(r'producto', ProductosViewSet)