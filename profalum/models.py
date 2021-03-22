from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    direccion_n = models.IntegerField()
    depto = models.CharField(max_length=255, null=True)
    dni = models.IntegerField()
    fecha_nac = models.DateField()

    def __str__(self):
        return f'Alumno {self.id}: {self.nombre} {self.apellido}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    direccion_n = models.IntegerField()
    depto = models.CharField(max_length=255, null=True)
    dni = models.IntegerField()
    fecha_nac = models.DateField()
    especializacion = models.CharField(max_length=255)
    notas = models.CharField(max_length=255)

    def __str__(self):
        return f'Profesor {self.id}: {self.nombre} {self.apellido}'


####DIAS DE LA SEMANA

DAY_OF_THE_WEEK = {
    '1' : _(u'Lunes'),
    '2' : _(u'Martes'),
    '3' : _(u'Miercoles'),
    '4' : _(u'Jueves'),
    '5' : _(u'Viernes'),
    '6' : _(u'Sabado'),
    '7' : _(u'Domigno'),
}

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)



class Horario(models.Model):
    horario = models.TimeField()
    dia = DayOfTheWeekField()
    profesor = models.CharField(max_length=255)
    clase = models.CharField(max_length=255)

    def __str__(self):
        return f'Horario {self.horario} {self.dia} {self.profesor} {self.clase}'


class HistorialFichas(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)

    def __str__(self):
        return f'HistorialFichas {self.nombre} {self.fecha}'


class Notas(models.Model):
    nota = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Notas {self.nota}'