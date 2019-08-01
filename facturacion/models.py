from django.db import models
from inventario.models import Producto
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(("Date"), default=datetime.date)
    impuesto = models.IntegerField()
    total = models.IntegerField()
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.total)
