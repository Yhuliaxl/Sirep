# apps/inventario/precios/models.py
from django.db import models
from apps.empresa.personas.models import cargo  # Ajusta la ruta según la ubicación real del modelo cargo
from apps.inventario.productos.models import Producto

class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    fk_cargo = models.ForeignKey(cargo,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Cargo asociado")
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Producto asociado",related_name="precios")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        producto_nombre = self.fk_producto.nombre if self.fk_producto else "Sin producto"
        return f"Precio {self.id_precio} - Producto {producto_nombre}"

    class Meta:
        verbose_name = "Precio"
        verbose_name_plural = "Precios"