from django.db import models
from apps.empresa.personas.models import persona

class PuntoVenta(models.Model):
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]

    id_punto_vent = models.AutoField(
        primary_key=True,
        verbose_name="Identificador único"
    )
    nombre = models.CharField(
        null=True,
        max_length=100,
        verbose_name="Nombre"
    )
    estado = models.CharField(
        max_length=8,
        choices=ESTADO_CHOICES,
        null=True,
        blank=True,
        verbose_name="Estado"
    )
    fecha_apertura = models.DateTimeField(
        null=True,
        auto_now_add=True,
        verbose_name="Fecha de apertura"
    )
    fecha_cierre = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de cierre"
    )
    saldo_inicial = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Saldo inicial"
    )
    saldo_final = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Saldo final"
    )
    observaciones = models.TextField(
        blank=True,
        verbose_name="Observaciones"
    )
    abierta_por = models.ForeignKey(
        persona,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cajas_abiertas',
        verbose_name="Abierta por"
    )
    cerrada_por = models.ForeignKey(
        persona,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cajas_cerradas',
        verbose_name="Cerrada por"
    )

    class Meta:
        db_table = 'punto_venta_caja'
        verbose_name = 'Punto de Venta Caja'
        verbose_name_plural = 'Puntos de Venta Caja'

    def __str__(self):
        return self.nombre