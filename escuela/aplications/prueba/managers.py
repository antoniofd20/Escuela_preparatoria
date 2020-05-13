from django.db import models

from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower
import datetime

class PersonaManager(models.Manager):

    def filtro_nombre(self, kword):
        resultado = self.filter(
            nombres__icontains = kword,
        )
        return resultado