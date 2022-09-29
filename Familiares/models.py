from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fecha_de_nacimiento=models.DateField()
    edad=models.IntegerField()
