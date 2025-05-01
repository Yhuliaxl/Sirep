# apps/inventario/inventario/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.db import connection
from apps.inventario.inventario.models import Inventario
from .serializers import InventarioSerializer

# Vista para renderizar la plantilla "dar-baja.html"
def render_dar_baja(request):
    return render(request, 'inventario/dar-baja.html', {'profile': request.user})

# ViewSet para manejar operaciones CRUD básicas sobre Inventario
class InventarioViewSet(ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

# Lista productos con stock (equivalente a Listar_Productos_Stock)
@api_view(['GET'])
def listar_productos_stock(request):
    try:
        # Consulta SQL simplificada (sin JOINs por ahora, ya que no tenemos los otros modelos)
        inventarios = Inventario.objects.filter(cantidad__gt=0).values(
            'id_inventario', 'id_producto', 'cantidad'
        )
        # Más adelante, cuando tengamos los modelos Producto y PuntoVenta, haremos los JOINs
        return Response(inventarios)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Crea un movimiento especial (equivalente a movimientoEspecial)
@api_view(['POST'])
def movimiento_especial(request):
    try:
        accion = request.data.get('accion')
        id_punto_venta = request.data.get('id_punto_venta')
        persona = None

        if accion == 'DarBaja':
            # Simulamos la lógica de obtención de persona (requiere modelo PuntoVenta)
            persona = id_punto_venta  # Placeholder
        else:
            persona = request.data.get('persona')

        # Simulamos la llamada al procedimiento almacenado (requiere modelo Movimiento)
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 AS Id_movimiento")  # Placeholder
            id_movimiento = cursor.fetchone()[0]

        return Response({'id_movimiento': id_movimiento, 'persona': persona})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Genera un detalle especial (equivalente a detalleEspecial)
@api_view(['POST'])
def detalle_especial(request):
    try:
        operacion = request.data.get('operacion')
        cantidad = request.data.get('cantidad')
        identificacion = request.data.get('identifiacion')
        descripcion = request.data.get('descripcion')
        movimiento = request.data.get('movimiento')
        inventario = request.data.get('inventario')

        # Simulamos la llamada al procedimiento almacenado (requiere modelo Detalle)
        with connection.cursor() as cursor:
            cursor.execute("SELECT 'success' AS result")  # Placeholder
            result = cursor.fetchone()[0]

        return Response({'result': result})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Registra un producto en un punto de venta (equivalente a registrarInventario)
@api_view(['POST'])
def registrar_inventario(request):
    try:
        id_producto = request.data.get('id_producto')
        id_punto_venta = request.data.get('id_punto_venta')

        # Validar si ya existe
        if Inventario.objects.filter(id_producto=id_producto, id_bodega=id_punto_venta).exists():
            return Response({'status': 'error', 'message': 'Este producto ya se encuentra asignado a P.V'})

        # Crear un nuevo registro en Inventario
        Inventario.objects.create(
            id_producto=id_producto,
            id_bodega=id_punto_venta,
            cantidad=0
        )

        return Response({'status': 'success', 'message': 'Producto asignado exitosamente'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Lista la distribución de una producción (equivalente a Listar_Distribucion)
@api_view(['POST'])
def listar_distribucion(request):
    try:
        id_produccion = request.data.get('id_produccion')
        # Consulta SQL simplificada (sin JOINs por ahora)
        distribuciones = Inventario.objects.filter(id_inventario=id_produccion).values(
            'id_inventario', 'id_bodega', 'fecha_actual', 'cantidad'
        )
        # Más adelante, cuando tengamos los modelos Produccion, Bodega y PuntoVenta, haremos los JOINs
        return Response(distribuciones)
    except Exception as e:
        return Response({'error': str(e)}, status=500)