"""samadhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from inicio.views import index, menu, alumnos, nuevoAlumno, eliminarAlumno, editarAlumno, profesores, nuevoProfesor, \
    editarProfesor, eliminarProfesor, crearFichas, verFichas, horarios, eliminarHorario, editarHorario, nuevoHorario, \
    eliminarFicha, notas, eliminarNota
from profalum.views import detalleAlumno, detalleProfesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home', notas, name='home'),
    path('home_eliminar/<int:id>', eliminarNota),

    path('alumnos', alumnos, name='alumnos'),
    path('detalle_alumno/<int:id>', detalleAlumno),
    path('nuevo_alumno', nuevoAlumno),
    path('editar_alumno/<int:id>', editarAlumno),
    path('eliminar_alumno/<int:id>', eliminarAlumno),

    path('profesores', profesores, name='profesores'),
    path('detalle_profesor/<int:id>', detalleProfesor),
    path('nuevo_profesor', nuevoProfesor),
    path('editar_profesor/<int:id>', editarProfesor),
    path('eliminar_profesor/<int:id>', eliminarProfesor),

    path('horarios', horarios, name='horarios'),
    path('nuevo_horario', nuevoHorario),
    path('editar_horario/<int:id>', editarHorario),
    path('eliminar_horario/<int:id>', eliminarHorario),

    path('ver_fichas', verFichas, name='ver_fichas'),
    path('crear_fichas', crearFichas, name='crear_fichas'),
    path('eliminar_ficha/<int:id>', eliminarFicha),

    path('accounts/', include('django.contrib.auth.urls'))
]
