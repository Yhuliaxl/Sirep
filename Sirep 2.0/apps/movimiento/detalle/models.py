from django.db import models
from apps.bodegas.punto_venta.models import PuntoVenta
from apps.movimiento.movimientos.models import Movimiento
from apps.inventario.inventario.models import Inventario
from apps.inventario.productos.models import Producto

class DetalleProduccion(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso'),
        ('Venta', 'Venta'),
    ]
    ENTREGADO_CHOICES = [
        ('Entregado', 'Entregado'),
        ('No entregado', 'No entregado'),
        ('No reclamado', 'No reclamado'),
    ]

    id_detalle = models.AutoField(
        primary_key=True,
        verbose_name="Identificador único"
    )
    tipo_movimiento = models.CharField(
        max_length=20,
        choices=TIPO_MOVIMIENTO_CHOICES,
        verbose_name="Tipo de movimiento"
    )
    cantidad = models.IntegerField(
        verbose_name="Cantidad"
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor"
    )
    persona = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name="Persona"
    )
    descripcion = models.TextField(
        verbose_name="Descripción"
    )
    fecha = models.DateTimeField(
        verbose_name="Fecha"
    )
    observacion = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Observación"
    )
    fk_punto_venta_caja = models.ForeignKey(
        PuntoVenta,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Caja asociada"
    )
    fk_movimiento_transaccion = models.ForeignKey(
        Movimiento,
        on_delete=models.CASCADE,
        verbose_name="Movimiento o transacción asociada"
    )
    fk_inventario = models.ForeignKey(
        Inventario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Inventario asociado"
    )
    fk_producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Producto asociado"
    )

    class Meta:
        db_table = 'detalle_produccion'
        verbose_name = 'Detalle Producción'
        verbose_name_plural = 'Detalles Producción'

    def __str__(self):
        return f"Detalle {self.id_detalle} - {self.tipo_movimiento}"