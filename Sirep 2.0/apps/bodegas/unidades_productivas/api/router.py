from rest_framework.routers import DefaultRouter
from .views import unidadProductivaViewSet

unidadProductivaRouter = DefaultRouter()
unidadProductivaRouter.register(r'unidadProductiva', unidadProductivaViewSet, basename='unidadProductiva')

urlpatterns = unidadProductivaRouter.urls 