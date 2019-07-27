from django.urls import path
from facturacion.forms import FacturaForm
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('facturar', views.facturaView, name='facturas'),

]