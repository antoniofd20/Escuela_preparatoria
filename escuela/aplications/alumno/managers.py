from django.db import models

from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower
import datetime

class AlumnoManager(models.Manager):

    def filtro_nombre(self, kword):
        resultado = self.filter(
            nombre_completo__icontains = kword,
        )
        return resultado