from django.shortcuts import render, get_object_or_404


# Create your views here.
from profalum.models import Alumno, Profesor


def detalleAlumno(request,id):
    alumno = get_object_or_404(Alumno, pk=id)
    return render(request, 'alumnos/detalle.html', {'alumno': alumno, 'nbar': 'alumnos'})

def detalleProfesor(request,id):
    profesor = get_object_or_404(Profesor, pk=id)
    return render(request, 'profesores/detalleprofe.html', {'profesor': profesor, 'nbar': 'profesores'})
