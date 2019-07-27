from django.urls import path
from inventario.forms import ProductoForm
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('nuevoProducto', login_required(views.producto_view), name='nuevoProducto'),
    path('', login_required(views.productoList_view), name='productoList'),
    path('nuevaMarca', login_required(views.agregarMarca_view), name='nuevaMarca'),
    path('nuevaCategoria', login_required(views.agregarCategoria_view), name='nuevaCategoria'),
    path('editarProducto/<int:codigo>/', login_required(views.productoActualizar_view), name='editarProducto'),
    path('eliminarProducto/<int:codigo>/', login_required(views.productoEliminar_view), name='eliminarProducto'),
    path('restList', views.ProductoListRest.as_view(), name='restListAll'),
]