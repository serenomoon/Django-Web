from django.forms import ModelForm, EmailInput
from django.utils.translation import ugettext_lazy as _
from profalum.models import Alumno, Profesor, Horario, Notas


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
        
class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'


class NotasForm(ModelForm):
    class Meta:
        model = Notas
        fields = ('nota',)
        labels = {
            'nota': _('')
        }
