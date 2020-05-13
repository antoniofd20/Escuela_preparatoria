from django.shortcuts import render
from django.views.generic import (
    ListView, FormView, UpdateView, DetailView, DeleteView
)
from django.urls import reverse_lazy

from .models import Alumno
from .forms import AlumnoForm

""" Lista de alumnos """
class AlumnoListView(ListView):
    template_name = "alumno/lista.html"
    model = Alumno
    context_object_name = 'lista'
    paginate_by = 2

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Alumno.objects.filtro_nombre(nombre)


""" Crear nuevo alumno """
class RegistrarAlumno(FormView): 
    template_name = "alumno/registrar.html"
    form_class = AlumnoForm
    success_url = reverse_lazy('alumno_app:lista-alumnos')

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
            f_baja = '2030-12-31',
            pago = form.cleaned_data['pago'],
            nombre_completo = form.cleaned_data['nombres'] + ' ' + form.cleaned_data['apellido_paterno'] +' ' + form.cleaned_data['apellido_materno'],
        )

        return super(RegistrarAlumno, self).form_valid(form)

""" Editar """
class AlumnoEditar(UpdateView):
    model = Alumno
    template_name = "alumno/editar.html"
    form_class = AlumnoForm
    success_url = reverse_lazy('alumno_app:lista-alumnos')

    def form_valid(self, form):
        alumno = form.save(commit=False)
        alumno.nombre_completo = alumno.nombres + ' ' + alumno.apellido_paterno + ' ' + alumno.apellido_materno
        alumno.save()
        return super(AlumnoEditar, self).form_valid(form)

""" Detalle """
class AlumnoDetalle(DetailView):
    template_name = "alumno/detalle.html"
    model = Alumno

""" Lista para eliminar """
class AlumnoEliminarListView(ListView):
    template_name = "alumno/lista_baja.html"
    model = Alumno
    context_object_name = 'lista'
    paginate_by = 2

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Alumno.objects.filtro_nombre(nombre)

""" Eliminar """
class AlumnoDeleteView(DetailView):
    model = Alumno
    template_name = "alumno/eliminar.html"

    success_url = reverse_lazy('alumno_app:lista-baja')