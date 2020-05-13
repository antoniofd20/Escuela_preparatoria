from django import forms

from aplications.prueba.models import Alumno, Profesor


class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = (
            'apellido_paterno',
            'apellido_materno',
            'nombres',
            'nacimiento',
            'edad',
            'sexo',
            'curp',
            'telefono',
            'celular',
            'tel_recado',
            'email',
            'calle_numero',
            'colonia',
            'municipio',
            'estado',
            'c_postal',
            'matricula',
            'f_baja',
            'pago',
        )

class ProfesorForm(forms.ModelForm):
    
    class Meta:
        model = Profesor
        fields = ('__all__')