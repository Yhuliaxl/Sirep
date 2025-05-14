from django.db import models

# Create your models here.
class CajaDiaria(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # abierta_por = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='cajas_abiertas')
    abierta_por = models.IntegerField(null=True, blank=True)  # Campo temporal reemplazando ForeignKey
    # cerrada_por = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='cajas_cerradas')
    cerrada_por = models.IntegerField(null=True, blank=True)  # Campo temporal reemplazando ForeignKey
    observaciones = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Caja Diaria"
        verbose_name_plural = "Cajas Diarias"

    def __str__(self):
        return self.nombre