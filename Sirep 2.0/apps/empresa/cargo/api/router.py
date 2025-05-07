from rest_framework.routers import DefaultRouter
from .views import cargoViewSet

cargoRouter = DefaultRouter()
cargoRouter.register(r'cargo', cargoViewSet, basename='cargo')

urlpatterns = cargoRouter.urls 