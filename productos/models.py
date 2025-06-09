from django.db import models

class Producto(models.Model):
    cod = models.CharField(max_length=40)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre