from django.db import models

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    # id_bodega = models.ForeignKey('bodegas.Bodega', on_delete=models.CASCADE, blank=True, null=True)
    # id_producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE, blank=True, null=True)
    id_bodega = models.IntegerField(blank=True, null=True)  # Temporalmente como IntegerField
    id_producto = models.IntegerField(blank=True, null=True)  # Temporalmente como IntegerField
    cantidad = models.IntegerField(blank=True, null=True)
    fecha_actual = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Inventario {self.id_inventario} - Producto {self.id_producto}"

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

# Create your models here.
