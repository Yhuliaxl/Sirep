from django.db import models

# Create your models here.

class Transacciones(models.Model):
    class Tipo(models.TextChoices):
        INGRESO = 'ingreso', 'Ingreso'
        EGRESO = 'egreso', 'Egreso'

    # caja = models.ForeignKey('CajaDiaria', on_delete=models.SET_NULL, null=True, related_name='transacciones')
    caja_id = models.IntegerField(null=True, blank=True)  # Campo temporal reemplazando ForeignKey
    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.INGRESO)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"

    def __str__(self):
        return f"{self.tipo} - {self.monto}"