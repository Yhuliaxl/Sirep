# apps/inventario/detalle/models.py
from django.db import models
from apps.movimiento.movimientos.models import Movimiento
from apps.inventario.inventario.models import Inventario

class Detalle(models.Model):
    ESTADO_CHOICES = [
        ('Facturado', 'Facturado'),
        ('Anulado', 'Anulado'),
        ('Prestamo', 'Prestamo'),
    ]
    ENTREGADO_CHOICES = [
        ('Entregado', 'Entregado'),
        ('No entregado', 'No entregado'),
        ('No reclamado', 'No reclamado'),
    ]

    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True, null=True)
    entregado = models.CharField(max_length=20, choices=ENTREGADO_CHOICES)
    persona = models.BigIntegerField(blank=True, null=True)
    fk_id_movimiento = models.ForeignKey(Movimiento,on_delete=models.CASCADE,verbose_name="Movimiento asociado",related_name="detalles")
    fk_id_inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE,verbose_name="Inventario asociado",related_name="detalles")

    def __str__(self):
        movimiento_id = self.fk_id_movimiento.id_movimiento if self.fk_id_movimiento else "Sin movimiento"
        return f"Detalle {self.id_detalle} - Movimiento {movimiento_id}"

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        
    