from django.contrib import admin
from django.urls import path

from . import views

app_name = 'profesor_app'

urlpatterns = [
    # Profesores
    # Lista 
    path(
        'lista-profesores/',
        views.ProfesorListView.as_view(),
        name = 'lista-profesores'
    ),
    # Registro 
    path(
        'registrar-profesor/',
        views.RegistrarProfesor.as_view(),
        name = 'registrar-profesor'
    ),
    # Editar
    path(
        'profesor/editar/<pk>/',
        views.ProfesorUpdateView.as_view(),
        name = 'editar-profesor'
    ),
    # Detalle
    path(
        'profesor/detalle/<pk>/',
        views.ProfesorDetailView.as_view(),
        name = 'detalle-profesor'
    ),
    # lista para eliminar
    path(
        'lista/profesores/baja/',
        views.ProfesorDeleteListView.as_view(),
        name = 'profesores-baja'
    ),
    # Eliminar
    path(
        'baja-definitiva/profesor/<pk>/',
        views.ProfesorDeleteView.as_view(),
        name = 'confirmar-baja'
    )
]
