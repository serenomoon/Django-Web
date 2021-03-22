# Generated by Django 3.1.7 on 2021-03-18 19:48

from django.db import migrations, models
import profalum.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('direccion_n', models.IntegerField()),
                ('depto', models.CharField(max_length=255, null=True)),
                ('dni', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HistorialFichas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('dia', profalum.models.DayOfTheWeekField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado'), ('7', 'Domigno')], max_length=1)),
                ('profesor', models.CharField(max_length=255)),
                ('clase', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('direccion_n', models.IntegerField()),
                ('depto', models.CharField(max_length=255, null=True)),
                ('dni', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('especializacion', models.CharField(max_length=255)),
                ('notas', models.CharField(max_length=255)),
            ],
        ),
    ]
