from django.shortcuts import render, redirect

# Create your views here.

from facturacion.models import Factura
from facturacion.forms import FacturaForm

def facturaView(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('facturaList')
    else:
        form = FacturaForm
    return render(request, 'facturacion/factura.html', {'form': form}) 