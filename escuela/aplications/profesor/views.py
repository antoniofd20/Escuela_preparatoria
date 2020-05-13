from django.shortcuts import render
from django.views.generic import (
    ListView, FormView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Profesor
from .forms import ProfesorForm

""" Lista de alumnos """
class ProfesorListView(ListView):
    template_name = "profesor/lista.html"
    model = Profesor
    context_object_name = 'lista'
    paginate_by = 2

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Profesor.objects.filtro_nombre(nombre)


""" Registro """
class RegistrarProfesor(FormView):
    template_name = "profesor/registrar.html"
    form_class = ProfesorForm
    success_url = '/lista-profesores/'

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
            nombre_completo = form.cleaned_data['nombres'] + ' ' + form.cleaned_data['apellido_paterno'] +' ' + form.cleaned_data['apellido_materno'],
        )

        return super(RegistrarProfesor, self).form_valid(form)

""" Editar """
class ProfesorUpdateView(UpdateView):
    model = Profesor
    template_name = "profesor/editar.html"

    form_class = ProfesorForm
    success_url = reverse_lazy('profesor_app:lista-profesores')

    def form_valid(self, form):
        profesor = form.save(commit=False)
        profesor.nombre_completo = profesor.nombres + ' ' + profesor.apellido_paterno + ' ' + profesor.apellido_materno
        profesor.save()
        return super(ProfesorUpdateView, self).form_valid(form)

""" Detalle """
class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "profesor/detalle.html"

""" Lista para eliminar """
class ProfesorDeleteListView(ListView):
    template_name = "profesor/lista_eliminar.html"
    model = Profesor
    context_object_name = 'lista'
    paginate_by = 2

    def get_queryset(self):
        nombre = self.request.GET.get("kword", '')
        return Profesor.objects.filtro_nombre(nombre)

""" Eliminar """
class ProfesorDeleteView(DetailView):
    model = Profesor
    template_name = "profesor/eliminar.html"

    success_url = reverse_lazy('profesor_app:profesores-baja')