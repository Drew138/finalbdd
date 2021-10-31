from django.db import models
from .choices import *
from django.contrib.postgres.fields import JSONField
# Create your models here.

# calendario --
# zona --
# rutina --
# persona --
# clase --
# equipo de clase --
# equipo de entrenamiento --

# !terminado
# registro de clase --


class Calendario(models.Model):  # TODO
    dia = models.CharField(
        max_length=255, choices=DiasEnum.choices, null=False, blank=False)  # enum
    hora_inicial = models.TimeField(null=False, blank=False)
    hora_final = models.TimeField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_final = models.DateField(null=False, blank=False)


class Zona(models.Model):

    piso = models.CharField(
        max_length=255, choices=PisosEnum.choices, null=False, blank=False)  # enum
    tipo = models.CharField(
        max_length=255, choices=TipoZonasEnum.choices, null=False, blank=False)  # enum


class RegistroDeClase(models.Model):
    persona = models.ForeignKey(
        'Persona', null=False, on_delete=models.CASCADE)
    calendario = models.ForeignKey(
        'Calendario', null=False, on_delete=models.CASCADE)
    clase = models.ForeignKey('Clase', null=False, on_delete=models.CASCADE)


class Rutina(models.Model):
    grupo_muscular = models.CharField(
        max_length=255, choices=GrupoMuscularEnum.choices, null=False, blank=False)  # enum
    cantidad_ejercicios = models.IntegerField(null=False, blank=False)
    dificultad = models.CharField(
        max_length=255, choices=DificultadesEnum.choices, null=False, blank=False)  # enum
    repeticiones = models.IntegerField(null=False, blank=False)
    lista_equipos = models.JSONField()  # TODO


class Persona(models.Model):

    nombre = models.CharField(max_length=255, null=False, blank=False)
    tipo = models.CharField(
        max_length=255, choices=TipoPersonaEnum.choices, null=False, blank=False)  # enum
    sexo = models.CharField(
        max_length=255, choices=SexoEnum.choices, null=False, blank=False)  # enum
    plan = models.CharField(
        max_length=255, choices=PlanPagoEnum.choices, null=False, blank=False)  # enum
    remuneracion = models.IntegerField(default=0)


class EquipoDeEntrenamiento(models.Model):

    nombre = models.CharField(max_length=255, null=False, blank=False)
    grupo_muscular = models.CharField(
        max_length=255, choices=GrupoMuscularEnum.choices, null=False, blank=False)  # enum
    zona = models.ForeignKey(
        'Zona', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_mantemiento = models.DateField(null=False, blank=False)
    fecha_adquisicion = models.DateField(null=False, blank=False)
    marca = models.CharField(max_length=255, null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)


class Clase(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    tipo = models.CharField(
        max_length=255, choices=TiposDeClaseEnum.choices, null=False, blank=False)  # enum
    costo = models.IntegerField(default=0)
    zona = models.ForeignKey(
        'Zona', null=True, blank=True, on_delete=models.SET_NULL)
    rutina = models.ForeignKey(
        'Rutina', null=False, blank=False, on_delete=models.CASCADE)
    maximo_personas = models.IntegerField(null=False, blank=False)
    equipos_de_entrenamiento = models.ManyToManyField(
        'EquipoDeEntrenamiento', blank=True)
