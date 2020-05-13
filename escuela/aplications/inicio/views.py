from django.shortcuts import render
from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name = "inicio/inicio.html"

class AlumnoView(TemplateView):
    template_name = "inicio/alumno.html"

class ProfesorView(TemplateView):
    template_name = "inicio/profesor.html"

class GrupoView(TemplateView):
    template_name = "inicio/grupo.html"

class PagoView(TemplateView):
    template_name = "inicio/pago.html"