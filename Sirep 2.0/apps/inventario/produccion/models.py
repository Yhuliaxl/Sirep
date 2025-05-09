# apps/inventario/produccion/models.py
from django.db import models
from apps.inventario.productos.models import Producto

class Produccion(models.Model):
    ESTADO_CHOICES = [
        ('Producido', 'Producido'),
        ('Aceptado', 'Aceptado'),
        ('Rechazado', 'Rechazado'),
    ]

    id_produccion = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True, null=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    observacion = models.CharField(max_length=50, blank=True, null=True)
    fk_codigo_pdto = models.ForeignKey(Producto,on_delete=models.CASCADE,verbose_name="Producto asociado",related_name="producciones")

    def __str__(self):
        producto_nombre = self.fk_codigo_pdto.nombre if self.fk_codigo_pdto else "Sin producto"
        return f"Produccion {self.id_produccion} - Producto {producto_nombre}"

    class Meta:
        verbose_name = "Produccion"
        verbose_name_plural = "Producciones"
        