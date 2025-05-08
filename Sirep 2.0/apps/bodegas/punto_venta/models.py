from django.db import models
from apps.empresa.personas.models import persona

class PuntoVenta(models.Model):
    CENTRO = 'Centro'
    YAMBORO = 'Yamboro'
    SEDE_CHOICES = [
        (CENTRO, 'Centro'),
        (YAMBORO, 'Yamboro'),
    ]

    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]

    id_punto_vent = models.AutoField(
        primary_key=True,
        verbose_name="ID del punto de venta"
    )
    sede = models.CharField(
        max_length=10,
        choices=SEDE_CHOICES,
        verbose_name="Sede",
    )
    direccion = models.IntegerField(
        verbose_name="Dirección"
    )
    nombre = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Nombre del punto de venta"
    )
    fk_persona = models.ForeignKey(
        persona,
        on_delete=models.PROTECT,
        verbose_name="Persona encargada",
        blank=True,  # Permitimos que sea opcional
        null=True
    )
    estado = models.CharField(
        max_length=8,
        choices=ESTADO_CHOICES,
        null=True,
        blank=True,
        verbose_name="Estado"
    )

    class Meta:
        db_table = 'punto_venta'
        verbose_name = 'Punto de Venta'
        verbose_name_plural = 'Puntos de Venta'

    def __str__(self):
        return f'Punto de Venta {self.id_punto_vent}'