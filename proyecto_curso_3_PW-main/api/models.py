from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_matricula = models.DateField()
    promedio = models.FloatField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Promedio: {self.promedio}"
