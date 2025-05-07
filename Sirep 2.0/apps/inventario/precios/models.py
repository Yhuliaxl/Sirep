from django.db import models

class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    # fk_cargo = models.ForeignKey('empresa.Cargo', on_delete=models.CASCADE, blank=True, null=True)
    # fk_producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE, blank=True, null=True)
    fk_cargo = models.IntegerField(blank=True, null=True)  # Temporalmente como IntegerField
    fk_producto = models.IntegerField(blank=True, null=True)  # Temporalmente como IntegerField
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Precio {self.id_precio} - Producto {self.fk_producto}"

    class Meta:
        verbose_name = "Precio"
        verbose_name_plural = "Precios"
        
# Create your models here.
