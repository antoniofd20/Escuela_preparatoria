from django import forms

from .models import Profesor

class ProfesorForm(forms.ModelForm):
    
    class Meta:
        model = Profesor
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
            'clave',
            'profesion',
            'especialidad',
            'rfc',
            'notas',
        )

        labels = {
            'apellido_paterno': 'Apellido paterno',
            'apellido_materno': 'Apellido materno',
            'nombres': 'Nombre(s)',
            'nacimiento': 'Fecha de nacimiento',
            'edad': 'Edad',
            'sexo':'Sexo',
            'curp': 'Curp',
            'telefono': 'Teléfono de casa',
            'celular': 'Celular',
            'tel_recado': 'Teléfono de emergencia',
            'email': 'Correo eléctronico',
            'calle_numero': 'Calle y numero',
            'colonia': 'Colonia',
            'municipio': 'Municipio',
            'estado': 'Estado',
            'c_postal': 'Código postal',
            'clave': 'Clave',
            'profesion': 'Profesión', 
            'especialidad': 'Especialidad',
            'rfc': 'RFC',
            'notas': 'Notas',
        }

        widgets = {
            'apellido_paterno': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellido paterno...'
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellido materno...'
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellido nombre(s)...'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ejemplo: 20/09/1999'
                }
            ),
            'edad': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Edad...'
                }
            ),
            'sexo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Sexo...'
                }
            ),
            'curp': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Curp...'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Número teléfonico...'
                }
            ),
            'celular': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Número celular...'
                }
            ),
            'tel_recado': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Número teléfonico de emergencia...'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo eléctronico...'
                }
            ),
            'calle_numero': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Calle y número...'
                }
            ),
            'colonia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Colonia...'
                }
            ),
            'municipio': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Municipio...'
                }
            ),
            'estado': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Estado...'
                }
            ),
            'c_postal': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Código postal...'
                }
            ),
            'clave': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Clave...'
                }
            ),
            'profesion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Profesión...'
                }
            ),
            'especialidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Especialidad...'
                }
            ),
            'rfc': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'RFC...'
                }
            ),
            'notas': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Notas...',
                    'rows': 3,
                }
            ),
        }