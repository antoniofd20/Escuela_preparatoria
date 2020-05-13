from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicio_app'

urlpatterns = [
    path(
        '',
        views.Inicio.as_view(),
        name='inicio'
    ),
    path(
        'alumno/',
        views.AlumnoView.as_view(),
        name='alumno'
    ),
    path(
        'profesor/',
        views.ProfesorView.as_view(),
        name='profesor'
    ),
    path(
        'grupo/',
        views.GrupoView.as_view(),
        name='grupo'
    ),
    path(
        'pago/',
        views.PagoView.as_view(),
        name='pago'
    ),
]