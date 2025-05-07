from rest_framework.routers import DefaultRouter
from .views import SenaEmpresaViewSet

senaEmpresaRouter = DefaultRouter()
senaEmpresaRouter.register(r'senaempresa', SenaEmpresaViewSet, basename='SenaEmpresa')