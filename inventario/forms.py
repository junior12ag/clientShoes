from django import forms
from inventario.models import Producto, Marca, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['nombre',]

    fields = [
        'nombre',
        'imagen',
        'marca',
        'modelo',
        'color',
        'size',
        'categoria',
        'cantidad',
        'precio_compra',
        'precio_venta',
        'descripcion',

    ]

    labels = {
        'nombre' : 'Nombre',
        'imagen' : 'Imagen',
        'marca' : 'Marca',
        'modelo': 'Modelo',
        'color' : 'Color',
        'size' : 'Size',
        'categoria' : 'Categoria',
        'cantidad' : 'Cantidad',
        'precio_compra' : 'Precio Compra',
        'precio_venta' : 'Precio Venta',
        'descripcion' : 'Descripcion',

    }

    widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'imagen': forms.ImageField(),
        'marca' : forms.TextInput(attrs={'class':'form-control'}),
        'modelo' : forms.TextInput(attrs={'class':'form-control'}),
        'color' : forms.TextInput(attrs={'class':'form-control'}),
        'size': forms.TextInput(attrs={'class':'form-control'}),
        'categoria' : forms.Select(attrs={'class' : 'form-control'}),
        'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
        'precio_compra' : forms.TextInput(attrs={'class':'form-control'}),
        'precio_venta': forms.TextInput(attrs={'class':'form-control'}),
        'descripcion': forms.TextInput(attrs={'class':'form-control'}),


    }

class MarcaForm(forms.ModelForm):
     class Meta:
         model = Marca
         exclude = []
fields = [
        'marca',
        
    ]
lables = {'marca': 'Marca'}
widgets = {'marca': forms.TextInput(attrs={'class': 'form-control'}),}


class CategoriaForm(forms.ModelForm):
     class Meta:
         model = Categoria
         exclude = []
fields = [
        'nombre',
        
    ]
lables = {'nombre': 'Nombre'}
widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),}

class ProductoFileForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['nombre',]