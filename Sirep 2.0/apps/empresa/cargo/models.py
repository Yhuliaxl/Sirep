from django.db import models

# Create your models here.
class cargo(models.Model):
    id_sena = models.AutoField(
        primary_key=True,
        verbose_name="Identificador único del cargo"
    )
    nombre = models.CharField(
        max_length=45,
        null=True,
        blank=True,
        verbose_name="Nombre del cargo"
    )
    num_factura = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Número consecutivo de facturación"
    )

    class Meta:
        db_table = 'cargo'
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.nombre or f'cargo {self.id_sena}'