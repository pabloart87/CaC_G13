from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('ingresar_datos', views.ingreso_datos, name= "ingresar_datos"),
    path('eliminar_datos', views.eliminar_datos, name= "eliminar_datos"),
    path("lista_mareografos", views.lista_mareografos.as_view(), name="lista_mareografos"),
    path("ver_detalles", views.ver_detalles.as_view(), name="ver_detalles"),
    path("consulta", views.consulta, name="consulta"),
    path("inicio", views.inicio, name="inicio"),
    path("alta_mareografo", views.alta_mareografo, name="alta_mareografo"),
    path("detalle_mareografos", views.detalle_mareografos, name="detalle_mareografos"),
]
