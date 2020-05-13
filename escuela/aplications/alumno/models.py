from django.db import models

from aplications.persona.models import Persona
from .managers import AlumnoManager

class Alumno(Persona):
    matricula = models.CharField('Matricula', max_length=10, unique=True)
    f_ingreso = models.DateField(auto_now=True)
    f_baja = models.DateField(auto_now=False, auto_now_add=False)
    pago = models.FloatField()

    objects = AlumnoManager()

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos' 
        ordering = ['nombre_completo']
