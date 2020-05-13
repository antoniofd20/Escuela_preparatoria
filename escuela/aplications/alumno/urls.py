from django.contrib import admin
from django.urls import path

from . import views

app_name = 'alumno_app'

urlpatterns = [
    # Lista alumnos
    path(
        'lista/alumnos/',
        views.AlumnoListView.as_view(),
        name = 'lista-alumnos'
    ),
    # Registro
    path(
        'registrar/nuevo/alumno/',
        views.RegistrarAlumno.as_view(),
        name = 'registrar-alumno'
    ),
    # Editar
    path(
        'editar/alumno/<pk>/',
        views.AlumnoEditar.as_view(),
        name = 'editar-alumno'
    ),
    # Detalle
    path(
        'detalle/alumno/<pk>/',
        views.AlumnoDetalle.as_view(),
        name = 'detalle-alumno'
    ),
    # Lista para eliminar
    path(
        'lista/alumnos/baja/',
        views.AlumnoEliminarListView.as_view(),
        name = 'lista-baja'
    ),
    # Eliminar alumno
    path(
        'baja-definitiva/alumno/<pk>/',
        views.AlumnoDeleteView.as_view(),
        name = 'confirmar-baja'
    )
]
