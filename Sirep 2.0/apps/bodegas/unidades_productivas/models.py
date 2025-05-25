# apps/inventario/unidades_productivas/models.py
from django.db import models
from apps.empresa.personas.models import persona
from apps.empresa.sena_empresa.models import senaEmpresa

class unidadProductiva(models.Model):

    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]

    codigo_up = models.AutoField(
        primary_key=True,
        verbose_name="Código único de la unidad productiva"
    )
    nombre = models.CharField(
        max_length=40,
        verbose_name="Nombre de la unidad productiva"
    )
    logo = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name="Logo de la unidad productiva"
    )
    descripcion = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Descripción corta de la unidad productiva"
    )
    estado = models.CharField(
        max_length=8,
        choices=ESTADO_CHOICES,
        null=True,
        blank=True,
        verbose_name="Estado"
    )
    #entrega_producto = models.BooleanField(
    #    verbose_name="Entrega de producto",
    #    help_text="True = entregado; False = reservado"
    #)
    fk_persona = models.ForeignKey(
        persona,
        on_delete=models.PROTECT,
        verbose_name="Persona encargada",
        blank=True,  # Permitimos que sea opcional
        null=True
    )

    #fk_sena_empresa = models.ForeignKey(
    #    senaEmpresa,
    #    on_delete=models.CASCADE,
    #    verbose_name="Empresa SENA asociada",
    #    related_name="unidades_productivas",
    #    blank=True,
    #    null=True
    #)
    
    class Meta:
        db_table = 'unidades_productivas'
        verbose_name = 'Unidad Productiva'
        verbose_name_plural = 'Unidades Productivas'

    def __str__(self):
        return f'{self.nombre} (Código {self.codigo_up})'