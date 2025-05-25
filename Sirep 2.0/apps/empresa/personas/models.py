# apps/empresa/personas/models.py
from django.db import models
from apps.empresa.cargo.models import cargo  # Ajusta la ruta según la ubicación real del modelo cargo

class persona(models.Model):

    identificacion = models.BigAutoField(
        primary_key=True,
        verbose_name="Identificador único de la persona"
    )
    nombre = models.CharField(
        max_length=80,
        verbose_name="Nombre de la persona"
    )
    correo = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Correo electrónico de la persona"
    )
    login = models.CharField(
        max_length=20,
        verbose_name="Nombre de usuario para ingreso"
    )
    password = models.CharField(
        max_length=15,
        verbose_name="Contraseña de ingreso a la plataforma"
    )
    direccion = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Dirección de residencia de la persona"
    )
    telefono = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Teléfono de la persona"
    )
    cargo = models.ForeignKey(
        cargo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Cargo que ocupa la persona"
    )
    ficha = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Ficha que pertenece la persona"
    )
    estado = models.BooleanField(
        default=True,
        verbose_name="Estado actual de la persona, si está activo o inactivo"
    )

    class Meta:
        db_table = 'personas'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        return self.nombre