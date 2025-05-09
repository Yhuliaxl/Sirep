# apps/inventario/productos/models.py
from django.db import models
from apps.bodegas.unidades_productivas.models import unidadProductiva

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    RESERVA_CHOICES = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    TIPO_CHOICES = [
        ('Venta', 'Venta'),
        ('Servicio', 'Servicio'),
    ]
    INVENTARIO_CHOICES = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]

    codigo_pdto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    imagen = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, blank=True, null=True)
    reserva = models.CharField(max_length=3, choices=RESERVA_CHOICES, blank=True, null=True)
    max_reserva = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    inventario = models.CharField(max_length=3, choices=INVENTARIO_CHOICES)
    fk_codigo_up = models.ForeignKey(unidadProductiva,on_delete=models.CASCADE,verbose_name="Unidad Productiva asociada",related_name="productos")

    def __str__(self):
        return f"Producto {self.nombre} (Código: {self.codigo_pdto})"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
