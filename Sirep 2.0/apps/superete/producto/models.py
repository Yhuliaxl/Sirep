from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    # categoria_id = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True)
    categoria_id = models.IntegerField(null=True, blank=True)  # Campo temporal reemplazando ForeignKey
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre