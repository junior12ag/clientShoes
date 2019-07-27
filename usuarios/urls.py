from django.urls import path
from inventario.forms import ProductoForm
from . import views

urlpatterns = [
    path('registrar', views.RegistroUsuario.as_view(), name='registrar')
   
]