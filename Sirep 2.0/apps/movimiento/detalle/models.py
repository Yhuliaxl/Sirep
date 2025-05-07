from django.db import models

class Detalle(models.Model):
    ESTADO_CHOICES = [
        ('Facturado', 'Facturado'),
        ('Anulado', 'Anulado'),
        ('Prestamo', 'Prestamo'),
    ]
    ENTREGADO_CHOICES = [
        ('Entregado', 'Entregado'),
        ('No entregado', 'No entregado'),
        ('No reclamado', 'No reclamado'),
    ]

    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True, null=True)
    entregado = models.CharField(max_length=20, choices=ENTREGADO_CHOICES)
    persona = models.BigIntegerField(blank=True, null=True)
    # fk_id_movimiento = models.ForeignKey('movimiento.Movimiento', on_delete=models.CASCADE)
    # fk_id_inventario = models.ForeignKey('inventario.Inventario', on_delete=models.CASCADE)
    fk_id_movimiento = models.IntegerField()  # Temporalmente como IntegerField
    fk_id_inventario = models.IntegerField()  # Temporalmente como IntegerField

    def __str__(self):
        return f"Detalle {self.id_detalle} - Movimiento {self.fk_id_movimiento}"

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        
        # Create your models here.
