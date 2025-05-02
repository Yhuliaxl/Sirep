from django.db import models

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
    # fk_codigo_pdto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    fk_codigo_pdto = models.IntegerField()  # Temporalmente como IntegerField

    def __str__(self):
        return f"Produccion {self.id_produccion} - Producto {self.fk_codigo_pdto}"

    class Meta:
        verbose_name = "Produccion"
        verbose_name_plural = "Producciones"

# Create your models here.
