from django.db import models

from aplications.persona.models import Persona
from .managers import ProfesorManager

class Profesor(Persona):
    clave = models.PositiveIntegerField('Clave')
    profesion = models.CharField('Profesión', max_length=20)
    especialidad = models.CharField('Especialidad', max_length=20)
    rfc = models.CharField('RFC', max_length=13)
    notas = models.TextField('Notas')

    objects = ProfesorManager()

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['nombre_completo']
