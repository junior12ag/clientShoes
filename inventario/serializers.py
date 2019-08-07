from inventario.models import Producto, Marca, Categoria
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['marca',]

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre',]

class ProductoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer(many=False, read_only=True)
    categoria = CategoriaSerializer(many=False, read_only=True)
    class Meta:
        model = Producto
        fields = [
        'codigoIQ',
        'imagen',
        'marca',
        'modelo',
        'color',
        'size',
        'categoria',
        'cantidad',
        'precio_venta',
        'descripcion',

    ]
   