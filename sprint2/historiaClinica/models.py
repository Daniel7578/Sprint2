from django.db import models
from medico.models import medico
from paciente.models import paciente


class HistoriaClinica(models.Model):
    doctores = models.ManyToManyField(medico)
    paciente = models.OneToOneField(paciente, on_delete=models.CASCADE,primary_key=True)
    activa = models.BooleanField(default=True)
    sintomas = models.TextField(max_length=500)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    ultimaModificacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.sintomas)