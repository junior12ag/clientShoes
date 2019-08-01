from facturacion.models import Factura
from rest_framework import serializers
from facturacion.models import Factura


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = [
            'productos',
            'fecha',
            'impuesto',
            'total',
            'cliente',
        ]

    def create(self, validate_data):
        instance = Factura()
        instance.productos = validate_data.get('productos')
        instance.fecha = validate_data.get('fecha')
        instance.impuesto = validate_data.get('impuesto')
        instance.total = validate_data.get('total')
        instance.cliente = validate_data.get('cliente')
        instance.save()
        return instance