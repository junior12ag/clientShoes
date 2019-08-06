from django.db import models
from inventario.models import Producto
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=15, null=True)
    impuesto = models.IntegerField()
    total = models.IntegerField()
    cliente = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.numero_factura)
