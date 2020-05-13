from django.contrib import admin
from django.urls import path

from . import views

name_app = 'prueba_app'

urlpatterns = [
    # Alumnos
    path(
        'lista/alumnos/prueba/',
        views.AlumnoListView.as_view(),
        name = 'lista-alumnos'
    ),
    path(
        'registrar/alumno/',
        views.RegistrarAlumno.as_view(),
        name = 'registrar-alumno'
    ),
    # Profesores
    path(
        'lista/profesores/',
        views.ProfesorListView.as_view(),
        name = 'lista-profesores'
    ),
    path(
        'registrar/profesor/',
        views.RegistrarProfesor.as_view(),
        name = 'registrar-profesor'
    ),
]
