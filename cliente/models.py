from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField(max_length=254, null=True)
    telefono = models.CharField(max_length=200, null=True)