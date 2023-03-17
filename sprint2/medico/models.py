from django.db import models

class medico(models.Model):
    especialidad = models.TextField(max_length=50)
    consultorio = models.TextField(max_length=50)
    def __str__(self):
        return '{}'.format(self.especialidad,self.consultorio)