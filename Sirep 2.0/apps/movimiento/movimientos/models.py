# apps/inventario/movimientos/models.py
from django.db import models

class Movimiento(models.Model):
    ESTADO_CHOICES = [
        ('Reservado', 'Reservado'),
        ('Facturado', 'Facturado'),
        ('Anulado', 'Anulado'),
        ('Prestamo', 'Prestamo'),
    ]
    TIPO_CHOICES = [
        ('Grupal', 'Grupal'),
        ('Individual', 'Individual'),
    ]

    id_movimiento = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    # fk_persona = models.ForeignKey('personas.Persona', on_delete=models.CASCADE)
    fk_persona = models.BigIntegerField()  # Temporalmente como BigIntegerField
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)
    num_factura = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Movimiento {self.id_movimiento} - Persona {self.fk_persona}"

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

# Create your models here.