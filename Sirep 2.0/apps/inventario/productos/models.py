from django.db import models
from apps.superete.categoria.models import Categoria
from apps.bodegas.unidades_productivas.models import unidadProductiva

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    TIPO_CHOICES = [
        ('Venta', 'Venta'), 
        ('Servicio', 'Servicio'),
    ]

    codigo_pdto = models.AutoField(
        primary_key=True,
        verbose_name="Código del producto"
    )
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre"
    )
    descripcion = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name="Descripción"
    )
    imagen = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name="Imagen"
    )
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        blank=True,
        null=True,
        verbose_name="Estado"
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        blank=True,
        null=True,
        verbose_name="Tipo"
    )

    precio_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Precio de compra"
    )
    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Precio de venta"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Stock"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría asociada"
    )
    fk_unidad_productiva = models.ForeignKey(
        unidadProductiva,
        on_delete=models.CASCADE,
        verbose_name="Unidad productiva asociada",
        blank=True,
        null=True
    )
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre