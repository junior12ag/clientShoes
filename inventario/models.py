from django.db import models

# Create your models here.

class Categoria(models.Model):
		nombre = models.CharField(max_length=50)
		def __str__(self):
			return self.nombre
		

class Marca(models.Model):
	marca = models.CharField(max_length=32)
	def __str__(self):
		return self.marca


class Producto(models.Model):
		codigoIQ = models.AutoField(primary_key=True)
		imagen = models.ImageField(null=True, blank=True, upload_to="media")
		nombre = models.CharField(max_length=50, null=True)
		marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
		modelo = models.CharField(max_length=15, null=True)
		color = models.CharField(max_length=15, null=True)
		size = models.CharField(max_length=10, null=True)
		categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
		cantidad = models.IntegerField(default=0)
		precio_compra = models.IntegerField()
		precio_venta = models.IntegerField()
		descripcion = models.CharField(max_length=600)
		def __str__(self):
			return self.nombre