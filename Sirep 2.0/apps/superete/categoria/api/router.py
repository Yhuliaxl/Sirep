from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

categoriaRouter = DefaultRouter()
categoriaRouter.register(r'categoria', CategoriaViewSet)