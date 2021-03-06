from django.db import models

# Create your models here.
class Persona(models.Model):

    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
    )

    """ Datos personales """
    apellido_paterno = models.CharField('Apellido paterno', max_length=20)
    apellido_materno = models.CharField('Apellido materno', max_length=20)
    nombres = models.CharField('Nombre(s)', max_length=20)
    nombre_completo = models.CharField('Nombre', max_length=60, blank=True)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    edad = models.PositiveIntegerField()
    sexo = models.CharField('Sexo', max_length=10)
    curp = models.CharField('Curp', max_length=18)
    #avatar = models.ImageField(upload_to='img/persona', blank=True)

    """ Datos de contacto """
    telefono = models.CharField('Telefono de casa', max_length=10)
    celular = models.CharField('Celular', max_length=10)
    tel_recado = models.CharField('Telefono de contacto', max_length=10)
    email = models.EmailField('Correo eléctronico')

    """ Datos de la residencia """
    calle_numero = models.CharField('Calle y numero', max_length=50)
    colonia = models.CharField('Colonia', max_length=30)
    municipio = models.CharField('Municipio', max_length=20)
    estado = models.CharField('Estado', max_length=15)
    c_postal = models.CharField('Código postal', max_length=5)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombres + ' ' + self.apellido_paterno + ' ' + self.apellido_materno