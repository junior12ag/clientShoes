from django.urls import path
from facturacion.forms import FacturaForm
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('facturar', views.facturaView, name='facturar'),
    path('restFac', views.FacturaRest.as_view(), name='restFac'),
    path('facturaList', views.FacturaList, name='facturaList'),
    path('facturaCreate', views.FacturaPost.as_view(), name='facturaCreate'),

]