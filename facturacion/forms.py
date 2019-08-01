from django import forms
from facturacion.models import Factura

class DateInput(forms.DateInput):
    input_type = 'date'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        exclude =['numero_factura']
    
    fields = [

        'productos',
        'fecha',
        'impuesto',
        'total',
        'cliente',
    ]

    labels = {
        'productos' : 'Productos',
        'fecha' : 'Fecha',
        'impuesto' : 'Impuestos',
        'total' : 'Total',
        'cliente' : 'Cliente',
    }

    widgets = {
        'productos' : forms.CheckboxSelectMultiple(),
        'fecha': forms.DateField(widget=DateInput),
        'impuesto' : forms.TextInput(attrs={'class' : 'form-control'}),
        'total' : forms.TextInput(attrs={'class' : 'form-control'}),
        'cliente' : forms.Select(attrs={'class': 'form-control'}),



    }