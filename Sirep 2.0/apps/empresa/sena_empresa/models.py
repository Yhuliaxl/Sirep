from django.db import models

class SenaEmpresa(models.Model):
    id_sena = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    num_factura = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre or "Sin nombre"

    class Meta:
        verbose_name = "Sena Empresa"
        verbose_name_plural = "Sena Empresas"
        
# Create your models here.
