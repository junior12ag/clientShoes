from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from facturacion.models import Factura
from facturacion.forms import FacturaForm
from facturacion.serializers import FacturaSerializer


def facturaView(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('facturaList')
    else:
        form = FacturaForm
    return render(request, 'facturacion/facturaForm.html', {'form': form}) 


class FacturaRest(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'],)
        return obj

def FacturaList(request):
    facturas = Factura.objects.all()
    contexto = {'facturas': facturas }
    return render(request, 'facturacion/facturaList.html', contexto)


#class FacturaPost(APIView):
#    def post(self, request):
#        serializer = FacturaSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED )
#        else:
#            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class FacturaPost(generics.CreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    def perform_create(self, serializer):
        factura = self.request.data = serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
