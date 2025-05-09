# apps/inventario/inventario/models.py
from django.db import models
from apps.bodegas.punto_venta.models import PuntoVenta
from apps.inventario.productos.models import Producto

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    fk_codigo_pdto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Producto asociado", related_name="inventarios_relacionados")
    fk_id_punto_vent = models.ForeignKey(PuntoVenta, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Punto venta asociado")
    cantidad = models.IntegerField(blank=True, null=True)
    fecha_actual = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Inventario {self.id_inventario} - Producto {self.fk_codigo_pdto}"

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

# Create your models here.
