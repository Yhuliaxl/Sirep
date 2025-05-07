from django.db import models

# Create your models here.
class senaEmpresa(models.Model):
    id_sena = models.AutoField(
        primary_key=True,
        verbose_name="Identificador único de SENA Empresa"
    )
    nombre = models.CharField(
        max_length=45,
        null=True,
        blank=True,
        verbose_name="Nombre de la empresa"
    )
    num_factura = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Número consecutivo de facturación"
    )

    class Meta:
        db_table = 'sena_empresa'
        verbose_name = 'SENA Empresa'
        verbose_name_plural = 'SENA Empresas'

    def __str__(self):
        return self.nombre or f'Empresa {self.id_sena}'
