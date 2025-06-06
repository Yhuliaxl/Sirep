"""
URL configuration for Sirep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# INVENTARIO
from apps.bodegas.bodega.api.router import bodegaRouter
from apps.bodegas.punto_venta.api.router import puntoVentaRouter
from apps.bodegas.unidades_productivas.api.router import unidadProductivaRouter

# EMPRESA
from apps.empresa.cargo.api.router import cargoRouter
from apps.empresa.personas.api.router import personaRouter
from apps.empresa.sena_empresa.api.router import senaEmpresaRouter

# INVENTARIO
from apps.inventario.inventario.api.router import inventarioRouter
from apps.inventario.precios.api.router import preciosRouter
#from apps.inventario.produccion.api.router import produccionRouter
from apps.inventario.productos.api.router import productosRouter

# MOVIMIENTO
from apps.movimiento.detalle.api.router import detalleRouter
from apps.movimiento.movimientos.api.router import movimientosRouter

#SUPERETE
##from apps.superete.caja_diaria.api.router import cajaDiariaRouter
from apps.superete.categoria.api.router import categoriaRouter
#from apps.superete.detalle_caja.api.router import detalleCajaRouter
#from apps.superete.producto.api.router import productoRouter
#from apps.superete.transacciones.api.router import transaccionesRouter


# ROUTERS
router = DefaultRouter()
routerBodega = DefaultRouter()
routerEempresa = DefaultRouter()
routerInventario = DefaultRouter()
routerMovimiento = DefaultRouter()
routerSuperete = DefaultRouter()

# ROUTERS BODEGA
routerBodega.registry.extend(bodegaRouter.registry)
routerBodega.registry.extend(puntoVentaRouter.registry)
routerBodega.registry.extend(unidadProductivaRouter.registry)

# ROUTERS EMPRESA
routerEempresa.registry.extend(cargoRouter.registry)
routerEempresa.registry.extend(personaRouter.registry)
routerEempresa.registry.extend(senaEmpresaRouter.registry)

# ROUTERS INVENTARIO
routerInventario.registry.extend(inventarioRouter.registry)
routerInventario.registry.extend(preciosRouter.registry)
#routerInventario.registry.extend(produccionRouter.registry)
routerInventario.registry.extend(productosRouter.registry)

# ROUTERS MOVIMIENTOS
routerMovimiento.registry.extend(detalleRouter.registry)
routerMovimiento.registry.extend(movimientosRouter.registry)

#ROUTER SUPERETE
#routerSuperete.registry.extend(cajaDiariaRouter.registry)
routerSuperete.registry.extend(categoriaRouter.registry)
#routerSuperete.registry.extend(detalleCajaRouter.registry)
#routerSuperete.registry.extend(productoRouter.registry)
#routerSuperete.registry.extend(transaccionesRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('bodega/', include(routerBodega.urls)),
    path('empresa/', include(routerEempresa.urls)),
    path('inventario/', include(routerInventario.urls)),
    path('movimiento/', include(routerMovimiento.urls)),  
    path('superete/', include(routerSuperete.urls)),
    # Rutas para Simple JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
