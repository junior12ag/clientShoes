from django.contrib import admin

# Register your models here.
from inventario.models import Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)