from django.db import models

class Perfil(models.Model):
    titulo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    tipo_puesto = models.CharField(max_length=100, choices=[
        ('remoto', 'Remoto'),
        ('presencial', 'Presencial'),
        ('hibrido', 'Híbrido'),
    ])
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateField(null=True, blank=True)
    link_aplicacion = models.URLField()

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"