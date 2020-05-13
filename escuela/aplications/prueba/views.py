from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from .models import Alumno, Profesor
from .forms import AlumnoForm, ProfesorForm

""" Vistas para los alumnos """
# Lista
class AlumnoListView(ListView):
    template_name = "alumno/lista.html"
    model = Alumno
    context_object_name = 'lista'

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Alumno.objects.filtro_nombre(nombre)

# Crear
class RegistrarAlumno(FormView):
    template_name = "alumno/registrar.html"
    form_class = AlumnoForm
    success_url = '/lista/alumnos/'

    def form_valid(self, form):
        Alumno.objects.create(
            apellido_paterno = form.cleaned_data['apellido_paterno'],
            apellido_materno = form.cleaned_data['apellido_materno'],
            nombres = form.cleaned_data['nombres'],
            nacimiento = form.cleaned_data['nacimiento'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            curp = form.cleaned_data['curp'],
            telefono = form.cleaned_data['telefono'],
            celular = form.cleaned_data['celular'],
            tel_recado = form.cleaned_data['tel_recado'],
            email = form.cleaned_data['email'],
            calle_numero = form.cleaned_data['calle_numero'],
            colonia = form.cleaned_data['colonia'],
            municipio = form.cleaned_data['municipio'],
            estado = form.cleaned_data['estado'],
            c_postal = form.cleaned_data['c_postal'],
            matricula = form.cleaned_data['matricula'],
            f_baja = form.cleaned_data['f_baja'],
            pago = form.cleaned_data['pago'],
        )

        return super(RegistrarAlumno, self).form_valid(form)



""" Vistas para los profesores """
# Lista
class ProfesorListView(ListView):
    template_name = "profesor/lista.html"
    model = Profesor
    context_object_name = 'lista'

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Profesor.objects.filtro_nombre(nombre)


# Crear
class RegistrarProfesor(FormView):
    template_name = "profesor/registrar.html"
    form_class = ProfesorForm
    success_url = '/lista/profesores/'

    def form_valid(self, form):
        Profesor.objects.create(
            apellido_paterno = form.cleaned_data['apellido_paterno'],
            apellido_materno = form.cleaned_data['apellido_materno'],
            nombres = form.cleaned_data['nombres'],
            nacimiento = form.cleaned_data['nacimiento'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            curp = form.cleaned_data['curp'],
            telefono = form.cleaned_data['telefono'],
            celular = form.cleaned_data['celular'],
            tel_recado = form.cleaned_data['tel_recado'],
            email = form.cleaned_data['email'],
            calle_numero = form.cleaned_data['calle_numero'],
            colonia = form.cleaned_data['colonia'],
            municipio = form.cleaned_data['municipio'],
            estado = form.cleaned_data['estado'],
            c_postal = form.cleaned_data['c_postal'],


            clave = form.cleaned_data['clave'],
            profesion = form.cleaned_data['profesion'],
            especialidad = form.cleaned_data['especialidad'],
            rfc = form.cleaned_data['rfc'],
            notas = form.cleaned_data['notas'],
        )

        return super(RegistrarProfesor, self).form_valid(form)
