from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
# Create your views here.


from django.http import HttpResponse
from inventario.forms import ProductoForm, MarcaForm, CategoriaForm, ProductoFileForm
from inventario.models import Producto
from inventario.serializers import ProductoSerializer

def index(request):
    return render(request, 'inventario/index.html')

def producto_view(request):
    if request.method == 'POST':
        form = ProductoFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('productoList')

    else:
        form = ProductoForm()
    return render(request, 'inventario/agregarProducto.html', {'form': form})

def productoActualizar_view(request, codigo):
    producto = Producto.objects.get(codigoIQ=codigo)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productoList')
    return render(request, 'inventario/agregarProducto.html', {'form': form})

def productoEliminar_view(request, codigo):
    producto = Producto.objects.get(codigoIQ=codigo)
    if request.method == 'POST':
        producto.delete()
        return redirect('productoList')
    return render(request, 'inventario/productoEliminar.html', {'producto': producto })

def productoDetalle_view(request, codigo):
    productos = Producto.objects.get(codigoIQ=codigo)
    return render(request, 'inventario/productoDetalle.html', {'productos' : productos })



def productoList_view(request):
    productos = Producto.objects.all().order_by('codigoIQ')
    contexto = {'productos': productos}
    return render(request, 'inventario/productoList.html', contexto)

def agregarMarca_view(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productoList')
    
    else:
        form = MarcaForm()
    return render(request, 'inventario/agregarMarca.html', {'form': form})

def agregarCategoria_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productoList')
    
    else:
        form = CategoriaForm()
    return render(request, 'inventario/agregarCategoria.html', {'form': form})

class ProductoListRest(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'],)
        return obj

class ProductoDetalleRest(generics.ListCreateAPIView):
 #   queryset = Producto.objects.get(codigoIQ=self.kwargs['codigo'])
    serializer_class = ProductoSerializer
    lookup_url_kwarg = "codigoIQ"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        respuesta = Producto.objects.filter(codigoIQ=uid)
        return respuesta


    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'],)
        return obj