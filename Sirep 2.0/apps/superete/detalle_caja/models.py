#apps.detalleCaja.models
from django.db import models
from django.db.models import SET_NULL
from apps.superete.caja_diaria.models import CajaDiaria
from apps.superete.transacciones.models import Transaccion

# Create your models here.
class Tipo(models.TextChoices):
    INGRESO = 'ingreso', 'Ingreso'
    EGRESO = 'egreso', 'Egreso'
    VENTA = 'venta', 'Venta'
class DetalleCaja(models.Model):
    fk_caja_id = models.ForeignKey(CajaDiaria, on_delete=SET_NULL, null=True)
    #caja_id = models.IntegerField(null=True, blank=True) # Campo temporal reemplazando ForeignKey
    fk_transaccion_id = models.ForeignKey(Transaccion, on_delete=SET_NULL, null=True)
    #transaccion_id = models.IntegerField(null=True, blank=True)  # Campo temporal reemplazando ForeignKey
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50, choices=Tipo.choices)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descripcion