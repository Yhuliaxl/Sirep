from django.db import models
from apps.empresa.personas.models import persona
from apps.inventario.productos.models import Producto

class Movimiento(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('Venta', 'Venta'),
        ('Compra', 'Compra'),
        ('Devolucion', 'Devolucion'),
        ('Ajuste', 'Ajuste'),
    ]

    id_movimiento = models.AutoField(
        primary_key=True,
        verbose_name="Identificador único"
    )
    tipo_movimiento = models.CharField(
        max_length=20,
        choices=TIPO_MOVIMIENTO_CHOICES,
        default='Reservado',
        verbose_name="Tipo de movimiento"
    )
    cantidad = models.IntegerField(
        default=0,
        verbose_name="Cantidad"
    )
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Precio unitario"
    )
    fecha = models.DateField(
        null=True,
        verbose_name="Fecha"
    )
    num_factura = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Número de factura"
    )
    fk_persona = models.ForeignKey(
        persona,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Persona asociada"
    )
    fk_producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Producto asociado"
    )

    class Meta:
        db_table = 'movimiento_transaccion'
        verbose_name = 'Movimiento Transacción'
        verbose_name_plural = 'Movimientos Transacciones'

    def __str__(self):
        return f"Movimiento {self.id_movimiento} - {self.tipo_movimiento}"