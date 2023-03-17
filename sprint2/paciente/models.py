from django.db import models

class paciente(models.Model):
    id = models.SmallIntegerField(null=False, blank=True, default=None, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    edad = models.SmallIntegerField(null=True, blank=True, default=None)
    sexo= models.CharField(max_length=10)
    fechaNacimiento = models.DateTimeField()
    prioridad = models.CharField(max_length=30)
    paisRecidencia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return '{}'.format(self.nombre, self.apellido, self.id)

# Create your models here.
