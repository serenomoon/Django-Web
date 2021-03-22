from django.shortcuts import render, redirect, get_object_or_404
import datetime

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Create your views here.
from profalum.forms import AlumnoForm, ProfesorForm, HorarioForm, NotasForm
from profalum.models import Alumno, Profesor, Horario, HistorialFichas, Notas


def index(request):
    return render(request, 'index.html')


def menu(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'nbar': 'home'})
    else:
        return redirect('index')


# ALUMNOS
def alumnos(request):
    if request.user.is_authenticated:
        no_alumnos = Alumno.objects.count()
        alumnos = Alumno.objects.order_by('nombre')
        return render(request, 'alumnos.html', {'no_alumnos': no_alumnos, 'alumnos': alumnos, 'nbar': 'alumnos'})
    else:
        return redirect('index')

def nuevoAlumno(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formaAlumno = AlumnoForm(request.POST)
            if formaAlumno.is_valid():
                formaAlumno.save()
                return redirect('alumnos')
        else:
            formaAlumno = AlumnoForm()

        return render(request, 'alumnos/nuevo.html', {'formaAlumno': formaAlumno, 'nbar': 'alumnos'})
    else:
        return redirect('index')

def editarAlumno(request, id):
    if request.user.is_authenticated:
        alumno = get_object_or_404(Alumno, pk=id)
        if request.method == 'POST':
            formaAlumno = AlumnoForm(request.POST, instance=alumno)
            if formaAlumno.is_valid():
                formaAlumno.save()
                return redirect('alumnos')
        else:
            formaAlumno = AlumnoForm(instance=alumno)

        return render(request, 'alumnos/editar.html', {'formaAlumno': formaAlumno, 'nbar': 'alumnos'})
    else:
        return render('index')

def eliminarAlumno(request, id):
    if request.user.is_authenticated:
        alumno = get_object_or_404(Alumno, pk=id)
        if alumno:
            alumno.delete()
        return redirect('alumnos')
    else:
        return redirect('index')


# FIN ALUMNOS


# PROFESORES
def profesores(request):
    if request.user.is_authenticated:
        no_profesores = Profesor.objects.count()
        profesores = Profesor.objects.order_by('nombre')
        return render(request, 'profesores.html',
                      {'no_profesores': no_profesores, 'profesores': profesores, 'nbar': 'profesores'})
    else:
        return redirect('index')

def nuevoProfesor(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formaProfesor = ProfesorForm(request.POST)
            if formaProfesor.is_valid():
                formaProfesor.save()
                return redirect('profesores')
        else:
            formaProfesor = ProfesorForm()

        return render(request, 'profesores/nuevoprofe.html', {'formaProfesor': formaProfesor, 'nbar': 'profesores'})
    else:
        return redirect('index')

def editarProfesor(request, id):
    if request.user.is_authenticated:
        profesor = get_object_or_404(Profesor, pk=id)
        if request.method == 'POST':
            formaProfesor = ProfesorForm(request.POST, instance=profesor)
            if formaProfesor.is_valid():
                formaProfesor.save()
                return redirect('profesores')
        else:
            formaProfesor = ProfesorForm(instance=profesor)

        return render(request, 'profesores/editarprofe.html', {'formaProfesor': formaProfesor, 'nbar': 'profesores'})
    else:
        return redirect('index')

def eliminarProfesor(request, id):
    if request.user.is_authenticated:
        profesor = get_object_or_404(Profesor, pk=id)
        if profesor:
            profesor.delete()
        return redirect('profesores')
    else:
        return redirect('index')


# FIN PROFESORES


# HORARIOS
def horarios(request):
    if request.user.is_authenticated:
        horarios = Horario.objects.order_by('dia', 'horario')
        return render(request, 'horarios.html', {'horarios': horarios, 'nbar': 'horarios'})
    else:
        return redirect('index')

def nuevoHorario(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formaHorario = HorarioForm(request.POST)
            if formaHorario.is_valid():
                formaHorario.save()
                return redirect('horarios')
        else:
            formaHorario = HorarioForm()

        return render(request, 'horarios/nuevohorario.html', {'formaHorario': formaHorario, 'nbar': 'horarios'})
    else:
        return redirect('index')

def editarHorario(request, id):
    if request.user.is_authenticated:
        horario = get_object_or_404(Horario, pk=id)
        if request.method == 'POST':
            formaHorario = HorarioForm(request.POST, instance=horario)
            if formaHorario.is_valid():
                formaHorario.save()
                return redirect('horarios')
        else:
            formaHorario = HorarioForm(instance=horario)

        return render(request, 'horarios/editarhorario.html', {'formaHorario': formaHorario, 'nbar': 'horarios'})
    else:
        return redirect('index')

def eliminarHorario(request, id):
    if request.user.is_authenticated:
        horario = get_object_or_404(Horario, pk=id)
        if horario:
            horario.delete()
        return redirect('horarios')
    else:
        return redirect('index')

# FIN PROFESORES
# FIN HORARIOS


# FICHAS
def verFichas(request):
    if request.user.is_authenticated:
        fichas = HistorialFichas.objects.order_by('nombre', 'fecha')
        return render(request, 'ver_fichas.html', {'nbar': 'asistencias', 'fichas': fichas})
    else:
        return redirect('index')

def eliminarFicha(request, id):
    if request.user.is_authenticated:
        ficha = get_object_or_404(HistorialFichas, pk=id)
        if ficha:
            ficha.delete()
        return redirect('ver_fichas')
    else:
        return redirect('index')


def crearFichas(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            seleccionados = request.POST.getlist('seleccionados')
            sint = []
            temp = []
            hingreso = []
            hegreso = []

            alumnos = Alumno.objects.order_by('nombre')

            # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()
            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)
            p.setFont("Helvetica", 9)
            espacion = 566
            time = datetime.date.today()
            fondo = ImageReader('https://i.ibb.co/VJfqrxY/cartilla.jpg')
            p.drawImage(fondo, 0, 0, width=595, height=850)
            p.drawString(270, 680, "Samadhi Studio")
            p.drawString(100, 664, "Avellaneda 362")
            p.drawString(76, 646, str(time))
            cuenta = -1
            for alumno in alumnos:
                for sel in seleccionados:
                    if sel == str(alumno.id):
                        if request.POST.get('sintomas' + str(alumno.id)) == None:
                            sint.append("No")
                        else:
                            sint.append(request.POST.get('sintomas' + str(alumno.id)))
                        temp.append(request.POST.get('temp' + str(alumno.id)))
                        hingreso.append(request.POST.get('hingreso' + str(alumno.id)))
                        hegreso.append(request.POST.get('hegreso' + str(alumno.id)))
                        cuenta += 1
                        espacion -= 16.1
                        p.drawString(15, espacion, str(alumno.nombre) + " " + str(alumno.apellido))
                        p.drawString(140, espacion, str(alumno.dni))
                        p.drawString(190, espacion, str(alumno.direccion) + " " + str(alumno.direccion_n))
                        p.drawString(335, espacion, str(alumno.telefono))
                        p.drawString(430, espacion, sint[cuenta] + "  " + temp[cuenta]+"°")
                        p.drawString(505, espacion, hingreso[cuenta])
                        p.drawString(550, espacion, hegreso[cuenta])
                        if espacion <= 100:
                            espacion = 530
                            p.showPage()
            # Cierra pdf
            p.save()

            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.
            buffer.seek(0)
            filename = 'r.clientes' + str(time) + '.pdf'
            hora = datetime.datetime.now().strftime("%X")

            hf =HistorialFichas(nombre=filename, fecha=hora)
            hf.save()

            return FileResponse(buffer, as_attachment=True, filename=filename)


            return redirect('home')
        else:
            alumnos = Alumno.objects.order_by('nombre')
            return render(request, 'crear_fichas.html', {'alumnos': alumnos, 'nbar': 'asistencias'})
    else:
        return redirect('index')



# FIN FICHAS


# NOTAS
def notas(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            notas = Notas.objects.order_by('-id')
            formaNota = NotasForm(request.POST)
            if formaNota.is_valid():
                formaNota.save()
                return redirect('home')
        else:
            formaNota = NotasForm()
            notas = Notas.objects.order_by('-id')

        return render(request, 'home.html', {'notas': notas,'formaNota': formaNota, 'nbar': 'home'})
    else:
        return redirect('index')


def eliminarNota(request, id):
    if request.user.is_authenticated:
        nota = get_object_or_404(Notas, pk=id)
        if nota:
            nota.delete()
        return redirect('home')
    else:
        return redirect('index')
