from django.db import models
from apps.inventario.inventario.models import Inventario
from apps.movimiento.detalle.models import DetalleProduccion

class Bodega(models.Model):
    id_bodega = models.AutoField(
        primary_key=True,
        verbose_name="ID de la bodega"
    )
    fecha = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de creación"
    )
    cantidad = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Capacidad máxima"
    )
    fk_inventario = models.ForeignKey(
        Inventario,
        on_delete=models.PROTECT,
        verbose_name="Inventario asociado",
        blank=True,
        null=True
    )
    fk_detalle_produccion = models.ForeignKey(  # Renombrado de fk_produccion a fk_detalle_produccion
        DetalleProduccion,
        on_delete=models.PROTECT,
        verbose_name="Producción asociada",
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'bodega'
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'

    def __str__(self):
        return f'Bodega {self.id_bodega}'